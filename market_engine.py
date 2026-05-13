import yfinance as yf
import pandas as pd

TICKERS = ["AAPL", "MSFT", "NVDA", "TSLA", "AMZN", "META", "GOOGL"]
BENCHMARK = "QQQ"

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

def compute_market_structure(data):
    returns = data.pct_change().dropna()
    benchmark_returns = returns[BENCHMARK]
    rows = []

    for ticker in TICKERS:
        r = returns[ticker]

        rolling_corr = r.rolling(WINDOW).corr(benchmark_returns)
        rolling_vol = r.rolling(WINDOW).std()
        relative_strength = data[ticker] / data[BENCHMARK]

        baseline_corr = rolling_corr.iloc[-BASELINE:].mean()
        baseline_vol = rolling_vol.iloc[-BASELINE:].mean()
        baseline_rs = relative_strength.iloc[-BASELINE:].mean()

        corr_drift = abs(rolling_corr.iloc[-1] - baseline_corr)
        vol_pressure = rolling_vol.iloc[-1] / baseline_vol
        rs_drift = (relative_strength.iloc[-1] - baseline_rs) / baseline_rs

        score = (
            corr_drift * 40
            + max(vol_pressure - 1, 0) * 35
            + abs(rs_drift) * 25
        )

        if score < 10:
            state = "STABLE"
        elif score < 25:
            state = "WATCH"
        elif score < 45:
            state = "STRUCTURAL DRIFT"
        else:
            state = "STRUCTURAL BREAK"

        rows.append({
            "ticker": ticker,
            "state": state,
            "structure_score": round(score, 2),
            "correlation_drift": round(corr_drift, 3),
            "volatility_pressure": round(vol_pressure, 2),
            "relative_strength_drift": round(rs_drift, 3),
        })

    return pd.DataFrame(rows).sort_values("structure_score", ascending=False)

if __name__ == "__main__":
    symbols = TICKERS + [BENCHMARK]
    data = get_data(symbols)
    output = compute_market_structure(data)

    print("\nMARKET STRUCTURE INTELLIGENCE\n")
    print(output.to_string(index=False))

    output.to_csv("market_structure_output.csv", index=False)

    print("\nSaved: market_structure_output.csv")
