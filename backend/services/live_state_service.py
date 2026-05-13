from market_sii.config.universe import SECTOR_UNIVERSE
from market_sii.data.providers.yahoo import fetch_close_prices
from market_sii.engines.market_topology_graph_engine import MarketTopologyGraphEngine
from market_sii.engines.multi_timeframe_engine import MultiTimeframeEngine
from market_sii.engines.breadth_engine import BreadthEngine
from market_sii.engines.liquidity_instability_engine import LiquidityInstabilityEngine
from market_sii.engines.drift_propagation_engine import DriftPropagationEngine
from market_sii.forecasting.structural_forecasting_engine import StructuralForecastingEngine
from market_sii.explanations.operator_explanation_engine import OperatorExplanationEngine
from market_sii.outputs.graph_payload import build_graph_payload


class LiveStateService:
    def __init__(self):
        self.topology_engine = MarketTopologyGraphEngine()
        self.multi_timeframe_engine = MultiTimeframeEngine()
        self.breadth_engine = BreadthEngine()
        self.liquidity_engine = LiquidityInstabilityEngine()
        self.propagation_engine = DriftPropagationEngine()
        self.forecasting_engine = StructuralForecastingEngine()
        self.explanation_engine = OperatorExplanationEngine()

    def snapshot(self):
        prices = fetch_close_prices(SECTOR_UNIVERSE)
        topology = self.topology_engine.run(prices)
        multi_timeframe = self.multi_timeframe_engine.run(prices)
        breadth = self.breadth_engine.evaluate(prices)
        liquidity = self.liquidity_engine.evaluate(prices)
        propagation = self.propagation_engine.propagation_score(multi_timeframe)

        drift_history = [v["topology_drift"] for v in multi_timeframe.values()]
        velocity_history = [v["drift_velocity"] for v in multi_timeframe.values()]
        acceleration_history = [v["drift_acceleration"] for v in multi_timeframe.values()]

        forecast = self.forecasting_engine.forecast_instability(
            drift_history=drift_history,
            velocity_history=velocity_history,
            acceleration_history=acceleration_history,
            topology_drift=topology["topology_drift"],
            propagation_score=propagation["propagation_score"],
            breadth_deterioration=breadth["breadth_deterioration"],
            liquidity_instability=liquidity["liquidity_instability"],
        )

        explanation = self.explanation_engine.explain(
            regime=forecast["forecast_outlook"],
            topology_drift=topology["topology_drift"],
            drift_velocity=sum(velocity_history),
            drift_acceleration=sum(acceleration_history),
            dominant_nodes=topology["dominant_nodes"],
        )

        graph = build_graph_payload(
            relationship_changes=topology["relationship_changes"],
            max_edges=40,
        )

        return {
            "system": "Market-SII",
            "topology": topology,
            "graph": graph,
            "multi_timeframe": multi_timeframe,
            "breadth": breadth,
            "liquidity": liquidity,
            "propagation": propagation,
            "forecast": forecast,
            "explanation": explanation,
        }
