from collections import deque
from dataclasses import dataclass, asdict
from datetime import datetime, timezone


@dataclass
class MarketStateSnapshot:
    regime: str
    topology_drift: float
    drift_velocity: float
    drift_acceleration: float
    edge_density: float
    timestamp: str

    @classmethod
    def from_values(
        cls,
        regime: str,
        topology_drift: float,
        drift_velocity: float,
        drift_acceleration: float,
        edge_density: float,
    ):
        return cls(
            regime=regime,
            topology_drift=float(topology_drift),
            drift_velocity=float(drift_velocity),
            drift_acceleration=float(drift_acceleration),
            edge_density=float(edge_density),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )


class StateHistory:
    def __init__(self, maxlen: int = 500):
        self.snapshots = deque(maxlen=maxlen)

    def append(self, snapshot: MarketStateSnapshot):
        self.snapshots.append(snapshot)

    def recent(self, n: int = 50):
        return [asdict(item) for item in list(self.snapshots)[-n:]]

    def latest(self):
        if not self.snapshots:
            return None
        return asdict(self.snapshots[-1])

    def transition_chain(self, n: int = 20):
        return [item.regime for item in list(self.snapshots)[-n:]]

    def persistence_score(self, regime: str, window: int = 10):
        recent = list(self.snapshots)[-window:]
        if not recent:
            return 0.0
        hits = sum(1 for item in recent if item.regime == regime)
        return hits / len(recent)
