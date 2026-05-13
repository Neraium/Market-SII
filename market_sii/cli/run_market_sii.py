from market_sii.config.universe import SECTOR_UNIVERSE
from market_sii.data.providers.yahoo import fetch_close_prices
from market_sii.engines.market_topology_graph_engine import MarketTopologyGraphEngine
from market_sii.engines.multi_timeframe_engine import MultiTimeframeEngine


if __name__ == "__main__":
    prices = fetch_close_prices(SECTOR_UNIVERSE)

    topology_engine = MarketTopologyGraphEngine()
    topology = topology_engine.run(prices)

    multi = MultiTimeframeEngine()
    timeframe_output = multi.run(prices)

    print("\nMARKET-SII\n")
    print("Topology Drift:", round(topology["topology_drift"], 4))
    print("Recent Edge Density:", round(topology["recent_edge_density"], 4))

    print("\nDOMINANT STRUCTURAL NODES\n")

    for node in topology["dominant_nodes"]:
        print(node)

    print("\nMULTI-TIMEFRAME STRUCTURE\n")

    for timeframe, values in timeframe_output.items():
        print(timeframe, values)
