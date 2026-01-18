from fastapi import APIRouter
from app.security.jwt import create_jwt

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/login")
def login(teacher_id: str, school_id: str):
    token = create_jwt({
        "teacher_id": teacher_id,
        "school_id": school_id,
        "role": "teacher"
    })
    return {"access_token": token}
