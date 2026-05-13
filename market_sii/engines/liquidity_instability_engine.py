import pandas as pd


class LiquidityInstabilityEngine:
    def evaluate(self, prices: pd.DataFrame, volumes: pd.DataFrame = None):
        returns = prices.pct_change().dropna()

        realized_volatility = returns.rolling(20).std().iloc[-1].mean()
        gap_risk = returns.abs().iloc[-1].mean()

        volume_instability = 0.0

        if volumes is not None:
            volume_instability = (
                volumes.pct_change().abs().rolling(20).mean().iloc[-1].mean()
            )

        instability = (
            realized_volatility * 0.5
            + gap_risk * 0.3
            + volume_instability * 0.2
        )

        return {
            "realized_volatility": round(float(realized_volatility), 6),
            "gap_risk": round(float(gap_risk), 6),
            "volume_instability": round(float(volume_instability), 6),
            "liquidity_instability": round(float(instability), 6),
        }
