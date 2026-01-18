from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from app.config import settings

security = HTTPBearer()

def get_current_teacher(token=Depends(security)):
    try:
        payload = jwt.decode(
            token.credentials,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGO],
        )
        return payload
    except JWTError:
        raise HTTPException(401, "Invalid token")
