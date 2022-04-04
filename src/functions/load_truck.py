from src.classes.truck import Truck
from src.classes.point import Point

def load_truck(truck: Truck, point: Point, cargos: [{}]):
    """
        Load the truck function with given amounts of specified cargos from certain point.
    @param truck: loaded truck
    @param point: loading point
    @param cargos: list of loaded cargos {type: amount}
    """

# potrzebna lista składana zwiększająca pole cargo
# obiektu Truck wg [{typ: ilosc}]
# ze zmiennej cargos wg [{typ: ilosc}]