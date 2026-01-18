from fastapi import APIRouter

router = APIRouter(prefix="/api/mentor", tags=["mentor"])

@router.get("/available")
def get_available_mentors():
    # TODO: Integrate with Elevate API
    return {
        "mentors": [],
        "message": "Mentor integration not yet implemented"
    }
