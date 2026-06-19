# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

# 1. Buat engine koneksi ke MySQL
engine = create_engine(settings.DATABASE_URL)

# 2. Buat sessionmaker untuk interaksi data (Query, Insert, Update)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Base class yang akan di-extend oleh model-model tabel kita nanti
Base = declarative_base()

# 4. Dependency Injection untuk digunakan di Router/Controller FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()