# app/utils/security.py
from datetime import datetime, timedelta, timezone
from typing import Optional
from passlib.context import CryptContext
from jose import jwt
from app.config import settings

# 1. Konfigurasi untuk enkripsi password menggunakan algoritma bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Mengubah password polos menjadi text acak yang tidak bisa dibaca"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Mengecek apakah password yang diinput cocok dengan versi enkripsi di DB"""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Membuat token JWT sebagai tiket masuk digital untuk user yang login"""
    to_encode = data.copy()
    
    # Mengatur waktu kedaluwarsa token
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Masukkan waktu expired ke dalam data token
    to_encode.update({"exp": expire})
    
    # Bungkus data menjadi JWT Token menggunakan Secret Key kita
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    
    return encoded_jwt