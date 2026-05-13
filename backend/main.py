from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.stream import router as stream_router
from backend.api.topology import router as topology_router
from backend.api.replay import router as replay_router
from backend.api.snapshot import router as snapshot_router
from backend.api.healthcheck import router as healthcheck_router
from backend.services.live_state_service import LiveStateService
from market_sii.config.settings import settings

app = FastAPI(title="Market-SII")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(stream_router)
app.include_router(topology_router)
app.include_router(replay_router)
app.include_router(snapshot_router)
app.include_router(healthcheck_router)

state_service = LiveStateService()


@app.get("/")
def root():
    return {
        "system": "Market-SII",
        "status": "online",
        "environment": settings.environment,
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
