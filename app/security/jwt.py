from datetime import datetime, timedelta
from jose import jwt
from app.config import settings

def create_jwt(payload: dict):
    data = payload.copy()
    data["exp"] = datetime.utcnow() + timedelta(
        minutes=settings.JWT_EXP_MIN
    )
    return jwt.encode(data, settings.JWT_SECRET, algorithm=settings.JWT_ALGO)
