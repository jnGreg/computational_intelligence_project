
from src.classes.transport_task import TransportTask
import random


def generate_task() -> TransportTask:
    """ For the daily transport task generates lists of:
            3 to 6 trucks of red, green or blue colour, parked in randomly chosen warehouse,
            400 to 600 points of coordinates x & y in range [0, 100]
                and cargo amount of [-200 to -100]U[100 to 200] kg of random cargo type for each,
            5 warehouses randomly chosen from the points list.

    :return TransportTask: generated transport task to solve later
    """

    n_points = random.randint(400, 600)
    points = []
    excluded = []
    cargo_types = ['tuna', 'uranium', 'oranges']
    i = 0
    while i < n_points:
        x = random.randint(*(0, 100))
        y = random.randint(*(0, 100))
        if (x, y) in excluded: continue
        excluded.append((x, y))
        cargo_amount = random.randint(100, 200)
        cargo_type = random.choice(cargo_types)
        points.append((x, y, cargo_amount, cargo_type))
        i += 1

    n_warehouses = 5
    warehouses = random.sample(points, n_warehouses)

    trucks = []
    n_trucks = random.randint(3, 6)
    truck_colours = ['red', 'green', 'blue']
    unload_time = 2

    for i in range(n_trucks):
        truck_colour = random.choice(truck_colours)
        if truck_colour == "red":
            capacity = 2000
            load_time = 3
            speed = 0.75
        elif truck_colour == "green":
            capacity = 1000
            load_time = 1
            speed = 1.5
        else:
            capacity = 1500
            load_time = 2
            speed = 1
        start_point = random.choice(warehouses)
        trucks.append((truck_colour, capacity, load_time, unload_time, speed, start_point))

    return TransportTask(warehouses, trucks, points)
