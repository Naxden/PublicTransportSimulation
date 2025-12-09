import simpy

class Stop(simpy.Resource):
    def __init__(self, env, name, capacity=1):
        super().__init__(env, capacity=capacity)
        self.name = name
        self.passengers = list()