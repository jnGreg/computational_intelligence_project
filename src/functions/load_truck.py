from src.classes.truck import Truck
from src.classes.point import Point
from functions.task_generator import generate_task

def load_truck(truck: Truck, point: Point, cargos: list=None):
    """
        Load the truck function with given amounts of specified cargo_amounts from certain point.
    @param truck: loaded truck
    @param point: loading point
    @param cargos: list of loaded cargo_amounts {type: amount}
    """

# potrzebna lista składana zwiększająca pole cargo_amount
    # potrzebna lista składana zwiększająca pole cargo_amount
    if truck.cargo_amount < truck.capacity:
        #narazie zakładamy że narazie ładujemy do pełna w magazynie 
        if point.magazine==True:
            truck.total_time=truck.total_time+(truck.capacity-truck.cargo_amount)*truck.load_speed
            truck.cargo_amount=truck.capacity
        else:
            if  point.cargo_amount>0:  
                if truck.capacity >= truck.cargo_amount+point.cargo_amount:
                    truck.total_time=truck.total_time+point.cargo_amount*truck.load_speed
                    truck.cargo_amount=truck.cargo_amount+point.cargo_amount    
                    point.cargo_amount=0
                else:
                    point.cargo_amount=point.cargo_amount-(truck.capacity-truck.cargo_amount)
                    truck.cargo_amount=truck.capacity

    return truck, point

# obiektu Truck wg [{typ: ilosc}]
# ze zmiennej cargo_amounts wg [{typ: ilosc}]
