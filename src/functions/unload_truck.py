from src.classes.truck import Truck
from src.classes.point import Point

def unload_truck(truck: Truck, point: Point, cargos: [{}]):
    """
        Unload the truck function with given amounts of specified cargos from certain point.
    @param truck: unloaded truck
    @param point: unloading point
    @param cargos: list of unloaded cargos {type: amount}
    """

# potrzebna lista składana zmniejszająca pole cargo
# obiektu Truck wg [{typ: ilosc}]
# ze zmiennej cargos wg [{typ: ilosc}]