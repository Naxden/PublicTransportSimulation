import random

from networkx.classes import DiGraph
from simpy import Environment

from data.Passenger import Passenger
from data.Stop import Stop
from utils.Constant import PASSENGER_MEAN_INTERARRIVAL


def passenger_generator(env: Environment, stops: dict[str, Stop], stops_graph: DiGraph, metrics):
    while True:
        yield env.timeout(random.expovariate(1.0 / PASSENGER_MEAN_INTERARRIVAL))

        while True:
            start_id = random.choice(list(stops.keys()))
            successors = list(stops_graph.successors(start_id))

            if successors:
                end_id = random.choice(successors)
                break  # znaleziono poprawne start/end

        passenger = Passenger(start_id, end_id, env.now)
        stops[start_id].passengers.append(passenger)
        metrics['generated'] += 1