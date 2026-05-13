import numpy as np


class StructuralForecastingEngine:
    def forecast_instability(
        self,
        drift_history,
        velocity_history,
        acceleration_history,
    ):
        drift_mean = float(np.mean(drift_history)) if drift_history else 0.0
        velocity_mean = float(np.mean(velocity_history)) if velocity_history else 0.0
        acceleration_mean = float(np.mean(acceleration_history)) if acceleration_history else 0.0

        instability_probability = (
            drift_mean * 0.5
            + velocity_mean * 0.3
            + acceleration_mean * 0.2
        )

        if instability_probability < 1:
            outlook = "stable"
        elif instability_probability < 2:
            outlook = "watch"
        elif instability_probability < 3:
            outlook = "elevated_instability"
        else:
            outlook = "critical_transition_risk"

        return {
            "forecast_score": round(float(instability_probability), 4),
            "forecast_outlook": outlook,
        }
