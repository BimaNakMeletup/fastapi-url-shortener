# app/models/url.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    
    # URL Asli (panjang) dan Kode Pendek uniknya
    long_url = Column(String(2048), nullable=False) # Panjang maksimal URL standar
    short_code = Column(String(50), unique=True, index=True, nullable=False)
    
    # Counter klik langsung (sesuai req: tanpa Redis dulu)
    clicks = Column(Integer, default=0, nullable=False)
    
    # Tanggal kedaluwarsa link (opsional, bisa kosong/null jika link abadi)
    expired_at = Column(DateTime, nullable=True)
    
    # Menghubungkan URL ke tabel users lewat id user (Foreign Key)
    # Dibuat nullable=True agar user anonim/tanpa login tetap bisa generate link dasar
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)

    # Kebalikan dari relasi di model User
    owner = relationship("User", back_populates="urls")