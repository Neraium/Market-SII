def map_market_subsystems():
    return {
        "growth_tech": ["QQQ", "XLK", "SMH", "NVDA", "AAPL", "MSFT"],
        "broad_equities": ["SPY", "IWM"],
        "financials": ["XLF"],
        "energy": ["XLE"],
        "crypto": ["BTC-USD", "ETH-USD"],
        "macro_fear": ["^VIX", "DX-Y.NYB", "^TNX"],
    }


def subsystem_pressure(relationship_changes, mapping):
    rows = []

    for subsystem, symbols in mapping.items():
        pressure = 0.0
        hits = 0

        for _, row in relationship_changes.iterrows():
            if row["left"] in symbols or row["right"] in symbols:
                pressure += abs(row["change"])
                hits += 1

        rows.append(
            {
                "subsystem": subsystem,
                "pressure": round(float(pressure), 4),
                "relationship_hits": hits,
            }
        )

    return sorted(rows, key=lambda x: x["pressure"], reverse=True)
