from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any


@dataclass
class MarketEvent:
    source: str
    symbol: str
    price: float
    size: float | None
    timestamp: str
    event_type: str = "trade"
    raw: dict[str, Any] | None = None

    def to_dict(self):
        return asdict(self)


def normalize_polygon_event(event: dict) -> MarketEvent | None:
    if not isinstance(event, dict):
        return None

    symbol = event.get("sym") or event.get("pair")
    price = event.get("p")
    size = event.get("s")
    timestamp = event.get("t")

    if symbol is None or price is None:
        return None

    return MarketEvent(
        source="polygon",
        symbol=str(symbol),
        price=float(price),
        size=float(size) if size is not None else None,
        timestamp=str(timestamp) if timestamp is not None else datetime.now(timezone.utc).isoformat(),
        raw=event,
    )


def normalize_binance_event(event: dict) -> MarketEvent | None:
    symbol = event.get("s")
    price = event.get("p")
    size = event.get("q")
    timestamp = event.get("T") or event.get("E")

    if symbol is None or price is None:
        return None

    return MarketEvent(
        source="binance",
        symbol=str(symbol),
        price=float(price),
        size=float(size) if size is not None else None,
        timestamp=str(timestamp) if timestamp is not None else datetime.now(timezone.utc).isoformat(),
        raw=event,
    )
