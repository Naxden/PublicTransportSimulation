import random
from data.Passenger import Passenger
from utils.Constant import PASSENGER_MEAN_INTERARRIVAL


def passenger_generator(env, stop, metrics):
    while True:
        yield env.timeout(random.expovariate(1.0 / PASSENGER_MEAN_INTERARRIVAL))
        destination_choice = random.choice(['C', 'D', 'E'])
        passenger = Passenger('A', destination_choice, env.now)
        stop.passengers.append(passenger)
        metrics['generated'] += 1
