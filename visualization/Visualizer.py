import networkx as nx
import matplotlib.pyplot as plt
from networkx import DiGraph


def visualize(gtfs_data, graph: DiGraph):
    pos = {
        stop["stop_id"]: (stop["stop_lon"], stop["stop_lat"])
        for _, stop in gtfs_data["stops"].iterrows()
    }

    labels = {node: data.get("label", node) for node, data in graph.nodes(data=True)}

    plt.figure(figsize=(12, 12))
    nx.draw(graph, pos, labels=labels, node_size=2, edge_color="black", alpha=0.2, with_labels=True)
    plt.show()