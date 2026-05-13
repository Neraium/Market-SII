import yfinance as yf


def fetch_close_prices(symbols, period="1y", interval="1d"):
    data = yf.download(
        symbols,
        period=period,
        interval=interval,
        auto_adjust=True,
        progress=False,
    )

    return data["Close"].dropna()
