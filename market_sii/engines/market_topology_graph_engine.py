from market_sii.config.timeframes import BASELINE_WINDOW
from market_sii.core.topology import topology_snapshot


class MarketTopologyGraphEngine:
    def __init__(self, recent_window: int = 30):
        self.recent_window = recent_window

    def run(self, prices):
        returns = prices.pct_change().dropna()

        snapshot = topology_snapshot(
            returns,
            baseline_window=BASELINE_WINDOW,
            recent_window=self.recent_window,
        )

        centrality = snapshot["centrality"]

        dominant_nodes = centrality.head(5).to_dict("records")

        return {
            "topology_drift": snapshot["topology_drift"],
            "baseline_edge_density": snapshot["baseline_edge_density"],
            "recent_edge_density": snapshot["recent_edge_density"],
            "dominant_nodes": dominant_nodes,
            "relationship_changes": snapshot["relationships"].head(25).to_dict("records"),
        }
