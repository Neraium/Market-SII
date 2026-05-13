import yfinance as yf
import pandas as pd
import numpy as np

TICKERS = ["AAPL", "MSFT", "NVDA", "TSLA", "AMZN", "META", "GOOGL"]

BASELINE = 120
WINDOWS = {
    "short_5d": 5,
    "swing_20d": 20,
    "trend_60d": 60,
}

def get_data(symbols):
    return yf.download(
        symbols,
        period="1y",
        interval="1d",
        auto_adjust=True,
        progress=False
    )["Close"].dropna()

def topology_score(returns, window):
    baseline_corr = returns.iloc[-BASELINE:].corr()
    recent_corr = returns.iloc[-window:].corr()
    return np.linalg.norm(recent_corr.values - baseline_corr.values)

if __name__ == "__main__":
    data = get_data(TICKERS)
    returns = data.pct_change().dropna()

    rows = []

    for name, window in WINDOWS.items():
        score = topology_score(returns, window)

        if score < 1.0:
            state = "STABLE"
        elif score < 2.0:
            state = "WATCH"
        elif score < 3.0:
            state = "STRUCTURAL DRIFT"
        else:
            state = "STRUCTURAL BREAK"

        rows.append({
            "timeframe": name,
            "window_days": window,
            "topology_score": round(score, 3),
            "state": state,
        })

    out = pd.DataFrame(rows)
    print("\nMULTI-TIMEFRAME MARKET STRUCTURE\n")
    print(out.to_string(index=False))

    out.to_csv("multi_timeframe_structure.csv", index=False)
    print("\nSaved: multi_timeframe_structure.csv")
