from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["system"])


@router.get("/ready")
def ready():
    return {"ready": True, "service": "Market-SII"}


@router.get("/live")
def live():
    return {"live": True}


@router.get("/version")
def version():
    return {"version": "0.1.0", "stage": "production-architecture-refactor"}
