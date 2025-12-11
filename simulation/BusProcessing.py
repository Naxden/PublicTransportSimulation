from utils.Constant import DOOR_OPERATION_TIME, TIME_PER_BOARD, TIME_PER_DEPARTURE, TRAVEL_TIME


def bus_process(env, bus_name, route, stops_map, capacity, metrics, start_delay=0.0):
  
    if start_delay > 0:
        yield env.timeout(start_delay)

    onboard = metrics['onboard'][bus_name]

    while True:
        for i, stop_name in enumerate(route):
            stop = stops_map[stop_name]

            with stop.request() as request:
                yield request
                print(f"{env.now:.1f}s: {bus_name} arrived at stop {stop_name}")
                to_departure = [passanger for passanger in list(onboard) if passanger.destination == stop_name]
                for departing_passanger in to_departure:
                    onboard.remove(departing_passanger)
                    departing_passanger.departure_timestamp = env.now
                    metrics['records'].append(departing_passanger)
                number_of_departured_passangers = len(to_departure)

                number_of_boarded_passengers = 0
                to_board = [p for p in stop.passengers if p.destination in route[i + 1:]]
                for b in to_board:
                    if len(onboard) < capacity:
                        stop.passengers.remove(b)
                        onboard.append(b)
                        b.board_timestamp = env.now
                        number_of_boarded_passengers += 1
                    else:
                        break

                onboarding_and_departure_time = DOOR_OPERATION_TIME + TIME_PER_BOARD * number_of_boarded_passengers + TIME_PER_DEPARTURE * number_of_departured_passangers
                yield env.timeout(onboarding_and_departure_time)
            print(f"{env.now:.1f}s: {bus_name} departed from stop {stop_name} (Boarded: {number_of_boarded_passengers}, Departured: {number_of_departured_passangers})")
            if i < len(route) - 1:
                yield env.timeout(TRAVEL_TIME)
                # Could switch to different travel times between stops
                # Could add traffic time delays here as well