import yfinance as yf
import pandas as pd
import numpy as np

SECTORS = ["SPY", "QQQ", "IWM", "XLK", "XLF", "XLE", "XLV", "XLI", "XLY", "XLP", "TLT", "GLD"]
BASELINE = 120
RECENT = 30

def get_data(symbols):
    return yf.download(
        symbols,
        period="1y",
        interval="1d",
        auto_adjust=True,
        progress=False
    )["Close"].dropna()

data = get_data(SECTORS)
returns = data.pct_change().dropna()

baseline_corr = returns.iloc[-BASELINE:].corr()
recent_corr = returns.iloc[-RECENT:].corr()
diff = recent_corr - baseline_corr

topology_score = np.linalg.norm(diff.values)

rows = []
for i, a in enumerate(SECTORS):
    for j, b in enumerate(SECTORS):
        if j <= i:
            continue
        rows.append({
            "relationship": f"{a} ↔ {b}",
            "baseline_corr": round(baseline_corr.loc[a, b], 3),
            "recent_corr": round(recent_corr.loc[a, b], 3),
            "change": round(recent_corr.loc[a, b] - baseline_corr.loc[a, b], 3),
            "abs_change": round(abs(recent_corr.loc[a, b] - baseline_corr.loc[a, b]), 3),
        })

out = pd.DataFrame(rows).sort_values("abs_change", ascending=False)

print("\nSECTOR TOPOLOGY INTELLIGENCE\n")
print("Market Topology Drift Score:", round(topology_score, 3))
print("\nTop Sector Relationship Changes\n")
print(out.head(20).to_string(index=False))

out.to_csv("sector_topology_changes.csv", index=False)
print("\nSaved: sector_topology_changes.csv")
