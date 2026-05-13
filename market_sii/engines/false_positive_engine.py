import numpy as np
import pandas as pd


class FalsePositiveEngine:
    def inject_noise(self, returns: pd.DataFrame, scale: float = 0.01):
        noise = np.random.normal(0, scale, returns.shape)
        return returns + noise

    def shuffled_series(self, returns: pd.DataFrame):
        shuffled = returns.copy()

        for column in shuffled.columns:
            shuffled[column] = np.random.permutation(shuffled[column].values)

        return shuffled

    def missing_data(self, returns: pd.DataFrame, fraction: float = 0.05):
        damaged = returns.copy()

        total = int(returns.size * fraction)

        for _ in range(total):
            i = np.random.randint(0, damaged.shape[0])
            j = np.random.randint(0, damaged.shape[1])
            damaged.iat[i, j] = np.nan

        return damaged.interpolate().dropna()

    def spike_burst(self, returns: pd.DataFrame, scale: float = 0.15):
        shocked = returns.copy()

        for column in shocked.columns:
            idx = np.random.randint(0, len(shocked))
            shocked.iloc[idx, shocked.columns.get_loc(column)] += np.random.normal(0, scale)

        return shocked
