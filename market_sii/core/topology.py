import numpy as np
import pandas as pd


def correlation_matrix(returns: pd.DataFrame) -> pd.DataFrame:
    return returns.corr()


def edge_density(corr: pd.DataFrame, threshold: float = 0.60) -> float:
    if corr.empty:
        return 0.0

    n = len(corr.columns)
    if n <= 1:
        return 0.0

    strong_edges = (corr.abs() > threshold).sum().sum() - n
    possible_edges = n * (n - 1)
    return float(strong_edges / possible_edges)


def relationship_changes(baseline_corr: pd.DataFrame, recent_corr: pd.DataFrame) -> pd.DataFrame:
    symbols = list(recent_corr.columns)
    rows = []

    for i, left in enumerate(symbols):
        for j, right in enumerate(symbols):
            if j <= i:
                continue

            baseline = baseline_corr.loc[left, right]
            recent = recent_corr.loc[left, right]
            change = recent - baseline

            rows.append(
                {
                    "left": left,
                    "right": right,
                    "relationship": f"{left} ↔ {right}",
                    "baseline_corr": round(float(baseline), 4),
                    "recent_corr": round(float(recent), 4),
                    "change": round(float(change), 4),
                    "abs_change": round(float(abs(change)), 4),
                }
            )

    return pd.DataFrame(rows).sort_values("abs_change", ascending=False)


def node_centrality(corr: pd.DataFrame, threshold: float = 0.60) -> pd.DataFrame:
    rows = []

    for symbol in corr.columns:
        links = corr[symbol].drop(symbol)
        strong_links = links[links.abs() > threshold]
        rows.append(
            {
                "symbol": symbol,
                "centrality": round(float(links.abs().mean()), 4),
                "strong_relationship_count": int(len(strong_links)),
                "relationship_pressure": round(float(strong_links.abs().sum()), 4),
            }
        )

    return pd.DataFrame(rows).sort_values("relationship_pressure", ascending=False)


def topology_snapshot(returns: pd.DataFrame, baseline_window: int, recent_window: int, threshold: float = 0.60):
    baseline = returns.iloc[-baseline_window:]
    recent = returns.iloc[-recent_window:]

    baseline_corr = correlation_matrix(baseline)
    recent_corr = correlation_matrix(recent)
    diff = recent_corr - baseline_corr

    return {
        "baseline_corr": baseline_corr,
        "recent_corr": recent_corr,
        "diff": diff,
        "topology_drift": float(np.linalg.norm(diff.values)),
        "baseline_edge_density": edge_density(baseline_corr, threshold),
        "recent_edge_density": edge_density(recent_corr, threshold),
        "relationships": relationship_changes(baseline_corr, recent_corr),
        "centrality": node_centrality(recent_corr, threshold),
    }
