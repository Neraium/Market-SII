from market_sii.forecasting.structural_forecasting_engine import StructuralForecastingEngine


def test_structural_transition_trigger():
    engine = StructuralForecastingEngine()

    result = engine.forecast_instability(
        drift_history=[1.6, 0.8, 1.1, 1.15],
        velocity_history=[0.0, 0.0, 0.0],
        acceleration_history=[0.0, 0.0, 0.0],
        topology_drift=3.1184,
        propagation_score=3.0,
        breadth_deterioration=0.2,
        liquidity_instability=0.012,
    )

    assert result['forecast_outlook'] == 'structural_transition'
