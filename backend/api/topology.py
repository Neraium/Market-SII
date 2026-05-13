from fastapi import APIRouter

router = APIRouter(prefix="/topology", tags=["topology"])


@router.get("/health")
def topology_health():
    return {
        "engine": "market_topology_graph_engine",
        "status": "online",
    }


@router.get("/relationships")
def topology_relationships():
    return {
        "relationships": [],
    }
