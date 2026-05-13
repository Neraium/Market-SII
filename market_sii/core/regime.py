def classify_regime(
    topology_drift,
    volatility_pressure,
    breadth_deterioration,
    drift_acceleration,
):
    if topology_drift < 1 and volatility_pressure < 1.1:
        return "stable_expansion"

    if topology_drift < 2 and drift_acceleration > 0:
        return "unstable_expansion"

    if breadth_deterioration > 0.4:
        return "compression"

    if topology_drift > 3 and volatility_pressure > 1.5:
        return "panic"

    if topology_drift > 2:
        return "transition"

    return "recovery"
