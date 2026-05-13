class DriftPropagationEngine:
    def propagation_score(self, timeframe_output):
        ordered = ["1m", "5m", "15m", "1h", "4h", "1d"]

        score = 0.0
        propagation_hits = []

        previous = None

        for tf in ordered:
            if tf not in timeframe_output:
                continue

            current = timeframe_output[tf]["topology_drift"]

            if previous is not None and current >= previous:
                score += 1
                propagation_hits.append(tf)

            previous = current

        return {
            "propagation_score": score,
            "propagating_timeframes": propagation_hits,
        }
