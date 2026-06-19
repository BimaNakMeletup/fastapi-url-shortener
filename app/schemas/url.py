# app/schemas/url.py
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

# 1. Skema data masuk saat membuat Short URL
class UrlCreate(BaseModel):
    long_url: HttpUrl          # Memastikan input berupa format URL website yang valid
    custom_alias: Optional[str] = None  # Opsional: jika user ingin menentukan string sendiri
    expired_in_hours: Optional[int] = None # Opsional: masa berlaku link dalam hitungan jam

# 2. Skema data keluar untuk merespons pembuatan link tunggal
class UrlResponse(BaseModel):
    id: int
    long_url: str
    short_code: str
    clicks: int
    expired_at: Optional[datetime] = None

    # Mengizinkan Pydantic membaca data langsung dari objek SQLAlchemy Model
    model_config = {"from_attributes": True}

# 3. Skema data keluar untuk daftar link di Dashboard User
class UserUrlsList(BaseModel):
    total_links: int
    links: list[UrlResponse]