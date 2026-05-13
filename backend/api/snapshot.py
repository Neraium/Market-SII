from fastapi import APIRouter

from backend.services.live_state_service import LiveStateService

router = APIRouter(prefix="/snapshot", tags=["snapshot"])
state_service = LiveStateService()


@router.get("/current")
def current_snapshot():
    return state_service.snapshot()


@router.get("/health-score")
def health_score():
    snapshot = state_service.snapshot()

    return {
        "forecast": snapshot["forecast"],
        "breadth": snapshot["breadth"],
        "liquidity": snapshot["liquidity"],
        "propagation": snapshot["propagation"],
    }
