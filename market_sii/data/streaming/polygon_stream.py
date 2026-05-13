import json
import os
import websockets

from market_sii.data.streaming.base import StreamingProvider


class PolygonStreamProvider(StreamingProvider):
    def __init__(self, api_key: str | None = None, feed: str = "stocks"):
        self.api_key = api_key or os.getenv("POLYGON_API_KEY")
        self.feed = feed
        self.websocket = None

    @property
    def url(self):
        if self.feed == "crypto":
            return "wss://socket.polygon.io/crypto"
        return "wss://socket.polygon.io/stocks"

    async def connect(self):
        if not self.api_key:
            raise ValueError("POLYGON_API_KEY is required")

        self.websocket = await websockets.connect(self.url)
        await self.websocket.send(json.dumps({"action": "auth", "params": self.api_key}))
        return self.websocket

    async def subscribe(self, symbols):
        if self.websocket is None:
            await self.connect()

        prefix = "XT" if self.feed == "crypto" else "T"
        params = ",".join([f"{prefix}.{symbol}" for symbol in symbols])
        await self.websocket.send(json.dumps({"action": "subscribe", "params": params}))

    async def stream(self):
        if self.websocket is None:
            await self.connect()

        async for message in self.websocket:
            yield json.loads(message)
