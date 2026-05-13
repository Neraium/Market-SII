import pandas as pd

from market_sii.live.rolling_state_engine import RollingStateEngine


class HistoricalReplayEngine:
    def __init__(self, symbols):
        self.engine = RollingStateEngine(symbols=symbols)

    def replay(self, prices: pd.DataFrame):
        outputs = []

        for timestamp, row in prices.iterrows():
            self.engine.update(timestamp, row.to_dict())

            if self.engine.ready():
                outputs.append(
                    {
                        "timestamp": str(timestamp),
                        "state": self.engine.evaluate(),
                    }
                )

        return outputs
