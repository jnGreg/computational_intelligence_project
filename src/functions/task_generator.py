
from src.classes.transport_task import TransportTask
import random


def generate_task() -> TransportTask:
    """ For the daily transport task generates lists of random:
            3 to 6 trucks of red, green or blue colour, parked in randomly chosen warehouse,
            400 to 600 points of coordinates x & y in range [0, 100]
                and cargo amount of [-200 to -100]U[100 to 200] kg of random cargo type for each,
            5 warehouses chosen from the points list.

    :return TransportTask: generated transport task to solve later
    """

    
