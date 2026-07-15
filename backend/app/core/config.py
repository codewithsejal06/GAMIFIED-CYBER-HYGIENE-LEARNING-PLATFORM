from dotenv import load_dotenv
from pathlib import Path
import os

# backend folder ka path
BASE_DIR = Path(__file__).resolve().parents[2]

# backend/.env load karega
load_dotenv(BASE_DIR / ".env")

class Settings:
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_PORT = os.getenv("DATABASE_PORT")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

settings = Settings()

print("HOST =", settings.DATABASE_HOST)
print("USER =", settings.DATABASE_USER)
print("PASSWORD =", settings.DATABASE_PASSWORD)