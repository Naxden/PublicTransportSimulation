from networkx import DiGraph
from simpy import Environment

from data.Stop import Stop

def generate_stops(env: Environment, stops_graph: DiGraph) -> dict[str, Stop]:
    stops = {}

    for stop_id in stops_graph.nodes():
        stops[stop_id] = Stop(env, stop_id, capacity=2)
    return stops