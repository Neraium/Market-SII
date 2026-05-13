class PolygonProvider:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def fetch_bars(self, symbols, timeframe="1m"):
        raise NotImplementedError(
            "Polygon integration scaffold added. Implement REST/websocket ingestion here."
        )
