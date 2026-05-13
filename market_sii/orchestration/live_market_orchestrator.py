import asyncio

from market_sii.data.normalization.market_events import (
    normalize_binance_event,
    normalize_polygon_event,
)


class LiveMarketOrchestrator:
    def __init__(self, providers=None):
        self.providers = providers or []
        self.handlers = []

    def register_handler(self, handler):
        self.handlers.append(handler)

    async def handle_event(self, event):
        normalized = None

        if event.get("ev"):
            normalized = normalize_polygon_event(event)
        elif event.get("s"):
            normalized = normalize_binance_event(event)

        if normalized is None:
            return

        for handler in self.handlers:
            await handler(normalized)

    async def run_provider(self, provider, symbols):
        await provider.connect()
        await provider.subscribe(symbols)

        async for event in provider.stream():
            if isinstance(event, list):
                for item in event:
                    await self.handle_event(item)
            else:
                await self.handle_event(event)

    async def run(self, symbols):
        tasks = [
            self.run_provider(provider, symbols)
            for provider in self.providers
        ]

        await asyncio.gather(*tasks)
