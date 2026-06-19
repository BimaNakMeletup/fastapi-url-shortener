# app/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    # Kolom-kolom tabel
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    # Relasi: Satu user bisa memiliki banyak URL (One-to-Many)
    # 'back_populates' menghubungkan model User dengan model Url
    urls = relationship("Url", back_populates="owner", cascade="all, delete-orphan")