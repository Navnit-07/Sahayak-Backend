from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    PROJECT_NAME = "Sahayak Backend"

    JWT_SECRET = os.getenv("JWT_SECRET", "change-me")
    JWT_ALGO = "HS256"
    JWT_EXP_MIN = 60 * 24 * 7

    COUCHDB_URL = os.getenv("COUCHDB_URL")
    COUCHDB_ADMIN = os.getenv("COUCHDB_ADMIN")
    COUCHDB_PASSWORD = os.getenv("COUCHDB_PASSWORD")

    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

    CHROMA_DIR = "./chroma_db"

settings = Settings()
