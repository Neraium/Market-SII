import json
from pathlib import Path

from market_sii.config.universe import SECTOR_UNIVERSE
from market_sii.data.providers.yahoo import fetch_close_prices
from market_sii.engines.market_topology_graph_engine import MarketTopologyGraphEngine
from market_sii.engines.multi_timeframe_engine import MultiTimeframeEngine
from market_sii.engines.breadth_engine import BreadthEngine
from market_sii.engines.liquidity_instability_engine import LiquidityInstabilityEngine
from market_sii.engines.drift_propagation_engine import DriftPropagationEngine
from market_sii.forecasting.structural_forecasting_engine import StructuralForecastingEngine
from market_sii.explanations.operator_explanation_engine import OperatorExplanationEngine


def main():
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    print("Fetching real market data from Yahoo Finance...")
    prices = fetch_close_prices(SECTOR_UNIVERSE, period="1y", interval="1d")

    print(f"Loaded price frame: {prices.shape[0]} rows x {prices.shape[1]} symbols")

    topology_engine = MarketTopologyGraphEngine()
    multi_timeframe_engine = MultiTimeframeEngine()
    breadth_engine = BreadthEngine()
    liquidity_engine = LiquidityInstabilityEngine()
    propagation_engine = DriftPropagationEngine()
    forecasting_engine = StructuralForecastingEngine()
    explanation_engine = OperatorExplanationEngine()

    topology = topology_engine.run(prices)
    multi_timeframe = multi_timeframe_engine.run(prices)
    breadth = breadth_engine.evaluate(prices)
    liquidity = liquidity_engine.evaluate(prices)
    propagation = propagation_engine.propagation_score(multi_timeframe)

    drift_history = [item["topology_drift"] for item in multi_timeframe.values()]
    velocity_history = [item["drift_velocity"] for item in multi_timeframe.values()]
    acceleration_history = [item["drift_acceleration"] for item in multi_timeframe.values()]

    forecast = forecasting_engine.forecast_instability(
        drift_history=drift_history,
        velocity_history=velocity_history,
        acceleration_history=acceleration_history,
        topology_drift=topology["topology_drift"],
        propagation_score=propagation["propagation_score"],
        breadth_deterioration=breadth["breadth_deterioration"],
        liquidity_instability=liquidity["liquidity_instability"],
    )

    explanation = explanation_engine.explain(
        regime=forecast["forecast_outlook"],
        topology_drift=topology["topology_drift"],
        drift_velocity=sum(velocity_history),
        drift_acceleration=sum(acceleration_history),
        dominant_nodes=topology["dominant_nodes"],
    )

    payload = {
        "symbols": list(prices.columns),
        "rows": len(prices),
        "topology": topology,
        "multi_timeframe": multi_timeframe,
        "breadth": breadth,
        "liquidity": liquidity,
        "propagation": propagation,
        "forecast": forecast,
        "explanation": explanation,
    }

    json_ready = json.loads(json.dumps(payload, default=str))

    with open(output_dir / "real_market_sii_snapshot.json", "w", encoding="utf-8") as file:
        json.dump(json_ready, file, indent=2)

    print("\nMARKET-SII REAL DATA SNAPSHOT")
    print("Symbols:", ", ".join(json_ready["symbols"]))
    print("Topology Drift:", round(json_ready["topology"]["topology_drift"], 4))
    print("Edge Density:", round(json_ready["topology"]["recent_edge_density"], 4))
    print("Forecast:", json_ready["forecast"])
    print("Explanation:", json_ready["explanation"]["summary"])
    print("\nSaved: outputs/real_market_sii_snapshot.json")


if __name__ == "__main__":
    main()
