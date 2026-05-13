import pandas as pd
import numpy as np

from market_sii.engines.false_positive_engine import FalsePositiveEngine


def build_returns():
    return pd.DataFrame(
        np.random.normal(0, 0.01, (200, 5)),
        columns=["A", "B", "C", "D", "E"],
    )


def test_noise_injection_runs():
    engine = FalsePositiveEngine()
    returns = build_returns()
    noisy = engine.inject_noise(returns)
    assert noisy.shape == returns.shape


def test_shuffle_runs():
    engine = FalsePositiveEngine()
    returns = build_returns()
    shuffled = engine.shuffled_series(returns)
    assert shuffled.shape == returns.shape


def test_missing_data_runs():
    engine = FalsePositiveEngine()
    returns = build_returns()
    repaired = engine.missing_data(returns)
    assert repaired.isna().sum().sum() == 0
