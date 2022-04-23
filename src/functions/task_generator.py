
from classes.transport_task import TransportTask
from classes.point import Point
from classes.truck import Truck

from random import randint, choice, sample


def generate_task() -> TransportTask:
    """ For the daily transport task generates lists of:
            3 to 6 trucks of red, green or blue colour, parked in randomly chosen warehouse,
            400 to 600 points of coordinates x & y in range [0, 100]
                and cargo amount of [-200 to -100]U[100 to 200] kg of random cargo type for each,
            5 warehouses randomly chosen from the points list.

    :return TransportTask: generated transport task to solve later
    """

    n_points = randint(400, 600)
    points = []
    excluded = []
    cargo_types = ['tuna', 'uranium', 'oranges']
    i = 0
    while i < n_points:
        x = randint(*(0, 100))
        y = randint(*(0, 100))
        if (x, y) in excluded: continue
        excluded.append((x, y))
        cargo_amount = randint(100, 200)*choice([-1, 1])
        cargo_type = choice(cargo_types)
        point={
               'location':(x, y),
               'cargo_amount':cargo_amount,
               'cargo_type': cargo_type,
               'magazine':False
            }
        points.append(point)
        i += 1

    n_warehouses = 5
    warehouses = sample(points, n_warehouses)
    for x in warehouses:
        x['magazine']=True
        x['cargo_amount']=0
        x['cargo_type']=None

    points.extend(warehouses)
    points=[Point(x['location'], x['magazine'],x['cargo_amount']) for x in points]

    trucks = []
    n_trucks = randint(3, 6)
    truck_colours = ['red', 'green', 'blue']
    warehouses=[x['location'] for x in warehouses]

    for i in range(n_trucks):
        truck_colour = choice(truck_colours)
        start_point = choice(warehouses)
        trucks.append(Truck(truck_colour, start_point))
        
    return TransportTask(trucks, points)
