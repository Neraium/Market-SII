import pandas as pd

from market_sii.config.timeframes import BASELINE_WINDOW
from market_sii.core.drift import (
    compute_drift_acceleration,
    compute_drift_velocity,
)
from market_sii.core.topology import topology_snapshot


class StructuralDriftEngine:
    def __init__(self, recent_window: int = 30):
        self.recent_window = recent_window
        self.previous_drift = None
        self.previous_velocity = None

    def run(self, prices: pd.DataFrame):
        returns = prices.pct_change().dropna()

        snapshot = topology_snapshot(
            returns=returns,
            baseline_window=BASELINE_WINDOW,
            recent_window=self.recent_window,
        )

        current_drift = snapshot["topology_drift"]

        velocity = 0.0
        acceleration = 0.0

        if self.previous_drift is not None:
            velocity = compute_drift_velocity(current_drift, self.previous_drift)

        if self.previous_velocity is not None:
            acceleration = compute_drift_acceleration(velocity, self.previous_velocity)

        self.previous_drift = current_drift
        self.previous_velocity = velocity

        snapshot["drift_velocity"] = velocity
        snapshot["drift_acceleration"] = acceleration

        return snapshot
