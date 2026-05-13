from fastapi import FastAPI

from backend.api.stream import router as stream_router
from backend.api.topology import router as topology_router
from backend.api.replay import router as replay_router
from backend.api.snapshot import router as snapshot_router
from backend.services.live_state_service import LiveStateService

app = FastAPI(title="Market-SII")

app.include_router(stream_router)
app.include_router(topology_router)
app.include_router(replay_router)
app.include_router(snapshot_router)

state_service = LiveStateService()


@app.get("/")
def root():
    return {
        "system": "Market-SII",
        "status": "online",
        "description": "Systemic market structure intelligence engine",
    }


@app.get("/health")
def health():
    return {
        "health": "stable"
    }


@app.get("/regime")
def regime():
    snapshot = state_service.snapshot()

    return {
        "forecast": snapshot["forecast"],
        "explanation": snapshot["explanation"],
    }


@app.get("/snapshot")
def snapshot():
    return state_service.snapshot()
