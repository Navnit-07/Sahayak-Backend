from pydantic import BaseModel
from typing import Dict

class TelemetryEvent(BaseModel):
    eid: str
    actor: str
    edata: Dict
