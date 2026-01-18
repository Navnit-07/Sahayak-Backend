from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.api import (
    health,
    auth,
    rag,
    telemetry,
    mentor,
)

app = FastAPI(title="Project Sahayak")

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(rag.router)
app.include_router(telemetry.router)
app.include_router(mentor.router)
