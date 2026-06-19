# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Membaca file .env
    model_config = SettingsConfigDict(env_file=".env")

# Inisialisasi agar bisa di-import di file lain
settings = Settings()