def market_health_payload(
    regime,
    topology_drift,
    drift_velocity,
    drift_acceleration,
    edge_density,
):
    return {
        "regime": regime,
        "topology_drift": round(float(topology_drift), 4),
        "drift_velocity": round(float(drift_velocity), 4),
        "drift_acceleration": round(float(drift_acceleration), 4),
        "edge_density": round(float(edge_density), 4),
    }


def subsystem_payload(symbol, pressure, centrality, state):
    return {
        "symbol": symbol,
        "pressure": round(float(pressure), 4),
        "centrality": round(float(centrality), 4),
        "state": state,
    }
