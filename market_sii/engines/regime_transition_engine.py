from market_sii.core.regime import classify_regime
from market_sii.memory.state_history import MarketStateSnapshot


class RegimeTransitionEngine:
    def build_snapshot(
        self,
        topology_drift,
        volatility_pressure,
        breadth_deterioration,
        drift_acceleration,
        edge_density,
    ):
        regime = classify_regime(
            topology_drift=topology_drift,
            volatility_pressure=volatility_pressure,
            breadth_deterioration=breadth_deterioration,
            drift_acceleration=drift_acceleration,
        )

        return MarketStateSnapshot.from_values(
            regime=regime,
            topology_drift=topology_drift,
            drift_velocity=volatility_pressure,
            drift_acceleration=drift_acceleration,
            edge_density=edge_density,
        )
