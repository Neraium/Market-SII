import asyncio
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(prefix="/stream", tags=["stream"])


@router.websocket("/market-state")
async def market_state_stream(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            await websocket.send_json(
                {
                    "system": "Market-SII",
                    "status": "streaming",
                    "regime": "transition",
                    "topology_drift": 0.0,
                    "edge_density": 0.0,
                    "message": "Live engine placeholder. Wire RollingStateEngine here.",
                }
            )
            await asyncio.sleep(2)
    except WebSocketDisconnect:
        return
