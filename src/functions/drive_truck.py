from classes.point import Point
from classes.truck import Truck
from gen_dist_matrix import calc_euc_dist

def drive_truck(truck:Truck,end_point: Point) -> Truck:
    """
        Function change location of the truck from current location to new destination and calculates distance and time it took.
    truck: Truck obj
    end_point: Point obj, destination
    """
    distance=calc_euc_dist(truck.location,end_point.location)
    truck.total_time=truck.total_time+distance*truck.speed*60
    truck.total_distance=truck.total_distance+distance
    truck.location=end_point.location
    return truck
