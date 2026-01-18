from fastapi import APIRouter

router = APIRouter(prefix="/api/sync", tags=["sync"])

@router.get("")
def sync_status():
    # TODO: Implement CouchDB sync check
    return {
        "status": "ok",
        "last_sync": None
    }
