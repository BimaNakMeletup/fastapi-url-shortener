# app/main.py
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from app.database import engine
from app.models import Base
from app.routers import auth, url

# 1. Buat tabel database otomatis
Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener API (Bit.ly Clone)", version="1.0.0")

# 2. Daftarkan API Routers
app.include_router(auth.router)
app.include_router(url.router)

# 3. Mount folder frontend untuk menyajikan file statis (HTML)
# Kita taruh di paling bawah agar tidak bentrok dengan routing short_code publik
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# 4. Route Root: Langsung menampilkan halaman utama frontend
@app.get("/")
def read_root():
    return FileResponse(os.path.join("frontend", "index.html"))