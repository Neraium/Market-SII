from market_sii.config.timeframes import TIMEFRAMES
from market_sii.engines.structural_drift_engine import StructuralDriftEngine


class MultiTimeframeEngine:
    def __init__(self):
        self.engines = {
            timeframe: StructuralDriftEngine(recent_window=window)
            for timeframe, window in TIMEFRAMES.items()
        }

    def run(self, prices):
        output = {}

        for timeframe, engine in self.engines.items():
            snapshot = engine.run(prices)
            output[timeframe] = {
                "topology_drift": snapshot["topology_drift"],
                "drift_velocity": snapshot["drift_velocity"],
                "drift_acceleration": snapshot["drift_acceleration"],
                "edge_density": snapshot["recent_edge_density"],
            }

        return output
