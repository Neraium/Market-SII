class BinanceProvider:
    def stream_trades(self, symbols):
        raise NotImplementedError(
            "Binance websocket scaffold added. Implement live stream ingestion here."
        )
