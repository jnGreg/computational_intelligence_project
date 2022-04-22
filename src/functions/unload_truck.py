from src.classes.truck import Truck
from src.classes.point import Point

def unload_truck(truck: Truck, point: Point, cargos: list=None):
    """
        Unload the truck function with given amounts of specified cargos from certain point.
    @param truck: unloaded truck
    @param point: unloading point
    @param cargos: list of unloaded cargos {type: amount}
    """
    if truck.cargo_amount>0:
        if point.magazine==True:
            truck.total_time=truck.total_time+truck.cargo_amount*truck.unload_speed
            truck.cargo_amount=0
        else:
            if point.cargo_amount<0:
                if truck.cargo_amount >= -point.cargo_amount:
                    truck.total_time=truck.total_time+ (-point.cargo_amount)*truck.speed
                    truck.cargo_amount=truck.cargo_amount+point.cargo_amount
                    point.cargo_amount=0
                    
                else:
                    point.cargo_amount=point.cargo_amount+truck.cargo_amount
                    truck.cargo_amount=0

    return truck, point
# potrzebna lista składana zmniejszająca pole cargo
# obiektu Truck wg [{typ: ilosc}]
# ze zmiennej cargos wg [{typ: ilosc}]