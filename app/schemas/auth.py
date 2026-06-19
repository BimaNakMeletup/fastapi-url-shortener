# app/schemas/auth.py
from pydantic import BaseModel, EmailStr
from typing import Optional

# 1. Skema untuk data masuk saat Register / Login
class UserCreate(BaseModel):
    email: EmailStr  # Pydantic otomatis mengecek apakah input berformat email valid (ada @ dan .com)
    password: str    # Memastikan password dikirim sebagai string

# 2. Skema untuk data keluar setelah berhasil Login (Token JWT)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# 3. Skema isi data di dalam Token (Payload) untuk validasi internal
class TokenData(BaseModel):
    user_id: Optional[int] = None