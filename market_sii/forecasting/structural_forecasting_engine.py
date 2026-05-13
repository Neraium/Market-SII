import numpy as np


class StructuralForecastingEngine:
    def forecast_instability(
        self,
        drift_history,
        velocity_history,
        acceleration_history,
        topology_drift=None,
        propagation_score=0.0,
        breadth_deterioration=0.0,
        liquidity_instability=0.0,
    ):
        drift_mean = float(np.mean(drift_history)) if drift_history else 0.0
        velocity_mean = float(np.mean(velocity_history)) if velocity_history else 0.0
        acceleration_mean = float(np.mean(acceleration_history)) if acceleration_history else 0.0
        topology_drift = float(topology_drift if topology_drift is not None else drift_mean)
        propagation_score = float(propagation_score or 0.0)
        breadth_deterioration = float(breadth_deterioration or 0.0)
        liquidity_instability = float(liquidity_instability or 0.0)

        forecast_score = (
            topology_drift * 0.45
            + drift_mean * 0.20
            + max(velocity_mean, 0.0) * 0.15
            + max(acceleration_mean, 0.0) * 0.10
            + propagation_score * 0.25
            + breadth_deterioration * 0.30
            + liquidity_instability * 5.0
        )

        if topology_drift >= 4.0 or propagation_score >= 4.0:
            outlook = "critical_transition_risk"
        elif topology_drift >= 3.0 or propagation_score >= 3.0:
            outlook = "structural_transition"
        elif topology_drift >= 2.0 or propagation_score >= 2.0 or forecast_score >= 2.0:
            outlook = "elevated_instability"
        elif topology_drift >= 1.0 or forecast_score >= 1.0:
            outlook = "watch"
        else:
            outlook = "stable"

        return {
            "forecast_score": round(float(forecast_score), 4),
            "forecast_outlook": outlook,
            "topology_drift": round(float(topology_drift), 4),
            "propagation_score": round(float(propagation_score), 4),
            "breadth_deterioration": round(float(breadth_deterioration), 4),
            "liquidity_instability": round(float(liquidity_instability), 6),
        }
