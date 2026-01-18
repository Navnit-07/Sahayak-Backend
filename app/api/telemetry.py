from fastapi import APIRouter, Depends
from app.models.telemetry import TelemetryEvent
from app.security.auth import get_current_teacher

router = APIRouter(prefix="/api/telemetry", tags=["telemetry"])

@router.post("")
def ingest(event: TelemetryEvent, teacher=Depends(get_current_teacher)):
    # Save to CouchDB OR forward to Sunbird
    print("Telemetry:", event.dict())
    return {"status": "ok"}
