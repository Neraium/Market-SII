def persistent_hits(series, threshold, confirmation_window=5, min_hits=3):
    hits = (series > threshold).rolling(confirmation_window).sum()
    return hits >= min_hits


def instability_state(p95_hits, p99_hits):
    if p99_hits:
        return "CONFIRMED_INSTABILITY"

    if p95_hits:
        return "WATCH"

    return "STABLE"
