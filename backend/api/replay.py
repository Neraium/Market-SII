from fastapi import APIRouter

router = APIRouter(prefix="/replay", tags=["replay"])


@router.get("/timeline")
def replay_timeline(limit: int = 100):
    return {
        "events": [],
        "limit": limit,
        "status": "placeholder",
    }
