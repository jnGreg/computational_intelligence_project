from src.classes.transport_task import TransportTask
from random import randint, choice, sample


def generate_task() -> TransportTask:
    """ For the daily transport task generates lists of:
            3 to 6 trucks of red, green or blue colour, parked in randomly chosen warehouse,
            400 to 600 points of coordinates x & y in range [0, 100]
                and cargo amount of [-200 to -100]U[100 to 200] kg of same cargo type for each,
            5 warehouses randomly chosen from the points list.
    :return TransportTask: generated transport task to solve later
    """

    n_points = randint(100, 200)
    points = []
    excluded = []
    # cargo_types = ['tuna', 'uranium', 'oranges']
    i = 0
    while i < n_points:
        x = randint(*(0, 100))
        y = randint(*(0, 100))
        if (x, y) in excluded:
            continue
        excluded.append((x, y))
        cargo_amount = randint(100, 200)*choice([-1, 1])
        # cargo_type = choice(cargo_types)
        points.append((x, y, cargo_amount))
        i += 1

    n_warehouses = 5
    warehouses = sample(points, n_warehouses)
    warehouses_new = []
    [warehouses_new.append(warehouses[index][:2]) for index, _ in enumerate(warehouses)]
    warehouses = warehouses_new

    trucks = []
    n_trucks = randint(3, 6)
    truck_colours = ['red', 'green', 'blue']
    unload_time = 2

    for i in range(n_trucks):
        colour = choice(truck_colours)
        start_point = choice(warehouses)
        trucks.append((colour, start_point))

    return TransportTask(trucks, points)
