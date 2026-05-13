import pandas as pd


class BreadthEngine:
    def evaluate(self, prices: pd.DataFrame):
        returns = prices.pct_change().dropna()

        advancing = (returns.iloc[-1] > 0).sum()
        declining = (returns.iloc[-1] < 0).sum()
        total = len(returns.columns)

        advance_decline_ratio = advancing / max(declining, 1)
        deterioration = declining / max(total, 1)

        return {
            "advancing": int(advancing),
            "declining": int(declining),
            "advance_decline_ratio": round(float(advance_decline_ratio), 4),
            "breadth_deterioration": round(float(deterioration), 4),
        }
