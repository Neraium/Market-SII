def build_graph_payload(relationship_changes, centrality=None, max_edges=40):
    nodes = {}
    edges = []

    for _, row in relationship_changes.head(max_edges).iterrows():
        left = row["left"]
        right = row["right"]

        nodes[left] = {
            "id": left,
            "label": left,
            "centrality": 0.0,
            "pressure": 0.0,
        }
        nodes[right] = {
            "id": right,
            "label": right,
            "centrality": 0.0,
            "pressure": 0.0,
        }

        edges.append(
            {
                "source": left,
                "target": right,
                "weight": abs(float(row["change"])),
                "change": float(row["change"]),
                "baseline_corr": float(row["baseline_corr"]),
                "recent_corr": float(row["recent_corr"]),
            }
        )

    if centrality is not None:
        for _, row in centrality.iterrows():
            symbol = row["symbol"]
            if symbol in nodes:
                nodes[symbol]["centrality"] = float(row.get("centrality", 0.0))
                nodes[symbol]["pressure"] = float(row.get("relationship_pressure", 0.0))

    return {
        "nodes": list(nodes.values()),
        "edges": edges,
    }
