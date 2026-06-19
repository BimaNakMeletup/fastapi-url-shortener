# app/routers/url.py
from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.database import get_db
from app.config import settings
from app.models.url import Url
from app.models.user import User
from app.schemas.url import UrlCreate, UrlResponse, UserUrlsList
from app.schemas.auth import TokenData
from app.utils.helpers import generate_short_code

router = APIRouter(tags=["URLs"])

# --- FUNGSI PENENGAH / DEPENDENCY UNTUK CEK JWT ---
def get_current_user(token: str = Depends(lambda: None), db: Session = Depends(get_db)):
    """Fungsi pembantu untuk memvalidasi JWT Token di endpoint terproteksi"""
    # Catatan: Di dunia nyata token diambil dari Header (OAuth2PasswordBearer).
    # Ini versi simpel untuk mengecek keabsahan token dari payload JWT.
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token tidak valid")
        token_data = TokenData(user_id=user_id)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token kedaluwarsa atau tidak valid")
        
    user = db.query(User).filter(User.id == token_data.user_id).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User tidak ditemukan")
    return user


# --- 1. ENDPOINT: GENERATE SHORT URL ---
@router.post("/shorten", response_model=UrlResponse, status_code=status.HTTP_201_CREATED)
def create_short_url(
    url_data: UrlCreate, 
    db: Session = Depends(get_db),
    # Kita buat token opsional lewat query string dulu agar mempermudah pengujian dasar
    token: str = None 
):
    # Cek apakah pembuatnya login (bawa token) atau anonim
    current_user_id = None
    if token:
        try:
            user = get_current_user(token, db)
            current_user_id = user.id
        except HTTPException:
            pass # Jika token salah, anggap dia anonim

    # Tentukan short code (Custom Alias atau Auto-generate)
    if url_data.custom_alias:
        code = url_data.custom_alias
        # Cek apakah alias sudah dipakai
        exists = db.query(Url).filter(Url.short_code == code).first()
        if exists:
            raise HTTPException(status_code=400, detail="Custom alias sudah digunakan!")
    else:
        # Generate string acak, ulangi kalau kebetulan tabrakan di DB
        while True:
            code = generate_short_code()
            exists = db.query(Url).filter(Url.short_code == code).first()
            if not exists:
                break

    # Hitung waktu expired jika diminta
    expired_at = None
    if url_data.expired_in_hours:
        expired_at = datetime.now(timezone.utc) + timedelta(hours=url_data.expired_in_hours)

    # Simpan ke DB
    new_url = Url(
        long_url=str(url_data.long_url),
        short_code=code,
        user_id=current_user_id,
        expired_at=expired_at
    )
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url


# --- 2. ENDPOINT: DASHBOARD USER (LIHAT SEMUA LINK BERDASARKAN JWT) ---
@router.get("/my-links", response_model=UserUrlsList)
def get_my_links(token: str, db: Session = Depends(get_db)):
    # Wajib bawa token valid
    user = get_current_user(token, db)
    
    # Ambil semua data link milik user tersebut
    user_links = db.query(Url).filter(Url.user_id == user.id).all()
    
    return {
        "total_links": len(user_links),
        "links": user_links
    }


# --- 3. ENDPOINT PUBLIK: REDIRECTION & CLICK COUNTER ---
@router.get("/{short_code}")
def redirect_to_long_url(short_code: str, db: Session = Depends(get_db)):
    # Cari kodenya di database
    url_entry = db.query(Url).filter(Url.short_code == short_code).first()
    
    if not url_entry:
        raise HTTPException(status_code=404, detail="Short URL tidak ditemukan!")
        
    # Cek apakah link sudah kedaluwarsa
    if url_entry.expired_at and url_entry.expired_at.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc):
        raise HTTPException(status_code=410, detail="Short URL ini sudah kedaluwarsa!")
        
    # Sesuai Req: Update counter klik langsung ke DB utama (tanpa Redis dulu)
    url_entry.clicks += 1
    db.commit()
    
    # Lakukan pengalihan halaman (Redirect 307 Temporary Redirect)
    return RedirectResponse(url=url_entry.long_url)