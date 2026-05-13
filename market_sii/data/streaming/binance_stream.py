import json
import websockets

from market_sii.data.streaming.base import StreamingProvider


class BinanceStreamProvider(StreamingProvider):
    def __init__(self):
        self.websocket = None

    async def connect(self):
        self.websocket = await websockets.connect("wss://stream.binance.com:9443/ws")
        return self.websocket

    async def subscribe(self, symbols):
        if self.websocket is None:
            await self.connect()

        payload = {
            "method": "SUBSCRIBE",
            "params": [f"{symbol.lower()}@trade" for symbol in symbols],
            "id": 1,
        }

        await self.websocket.send(json.dumps(payload))

    async def stream(self):
        if self.websocket is None:
            await self.connect()

        async for message in self.websocket:
            yield json.loads(message)
