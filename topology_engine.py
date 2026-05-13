import yfinance as yf
import pandas as pd
import numpy as np

TICKERS = ["AAPL", "MSFT", "NVDA", "TSLA", "AMZN", "META", "GOOGL"]
WINDOW = 30
BASELINE = 120

def get_data(symbols):
    return yf.download(
        symbols,
        period="1y",
        interval="1d",
        auto_adjust=True,
        progress=False
    )["Close"].dropna()

def run_topology(data):
    returns = data.pct_change().dropna()

    baseline = returns.iloc[-BASELINE:]
    recent = returns.iloc[-WINDOW:]

    baseline_corr = baseline.corr()
    recent_corr = recent.corr()

    diff = recent_corr - baseline_corr

    rows = []

    for i, a in enumerate(TICKERS):
        for j, b in enumerate(TICKERS):
            if j <= i:
                continue

            base = baseline_corr.loc[a, b]
            now = recent_corr.loc[a, b]
            change = now - base

            rows.append({
                "relationship": f"{a} ↔ {b}",
                "baseline_corr": round(base, 3),
                "recent_corr": round(now, 3),
                "change": round(change, 3),
                "abs_change": round(abs(change), 3),
            })

    relationships = pd.DataFrame(rows).sort_values("abs_change", ascending=False)

    topology_score = np.linalg.norm(diff.values)

    edge_density_baseline = ((baseline_corr.abs() > 0.6).sum().sum() - len(TICKERS)) / (len(TICKERS) * (len(TICKERS) - 1))
    edge_density_recent = ((recent_corr.abs() > 0.6).sum().sum() - len(TICKERS)) / (len(TICKERS) * (len(TICKERS) - 1))

    print("\nMARKET TOPOLOGY INTELLIGENCE\n")
    print("Topology Drift Score:", round(topology_score, 3))
    print("Baseline Edge Density:", round(edge_density_baseline, 3))
    print("Recent Edge Density:", round(edge_density_recent, 3))
    print("Edge Density Change:", round(edge_density_recent - edge_density_baseline, 3))

    print("\nTOP RELATIONSHIP CHANGES\n")
    print(relationships.head(15).to_string(index=False))

    relationships.to_csv("market_topology_relationship_changes.csv", index=False)

if __name__ == "__main__":
    data = get_data(TICKERS)
    run_topology(data)
