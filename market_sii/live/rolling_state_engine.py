from collections import deque
import pandas as pd

from market_sii.engines.market_topology_graph_engine import MarketTopologyGraphEngine
from market_sii.engines.multi_timeframe_engine import MultiTimeframeEngine


class RollingStateEngine:
    def __init__(self, symbols, max_points: int = 1000):
        self.symbols = symbols
        self.max_points = max_points
        self.price_buffer = {symbol: deque(maxlen=max_points) for symbol in symbols}
        self.timestamp_buffer = deque(maxlen=max_points)
        self.topology_engine = MarketTopologyGraphEngine()
        self.multi_timeframe_engine = MultiTimeframeEngine()

    def update(self, timestamp, prices: dict):
        self.timestamp_buffer.append(timestamp)

        for symbol in self.symbols:
            self.price_buffer[symbol].append(prices.get(symbol))

    def ready(self, min_points: int = 150):
        return len(self.timestamp_buffer) >= min_points

    def prices_frame(self):
        return pd.DataFrame(
            {symbol: list(values) for symbol, values in self.price_buffer.items()},
            index=list(self.timestamp_buffer),
        ).dropna()

    def evaluate(self):
        prices = self.prices_frame()

        if prices.empty:
            return {
                "status": "insufficient_data",
            }

        topology = self.topology_engine.run(prices)
        multi_timeframe = self.multi_timeframe_engine.run(prices)

        return {
            "status": "evaluated",
            "topology": topology,
            "multi_timeframe": multi_timeframe,
        }
