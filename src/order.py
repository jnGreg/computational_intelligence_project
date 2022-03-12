
from point import Point
from truck import Truck


class Order:
    def __init__(self, point: Point, truck: Truck):
        self._point = point
        self._truck = truck

    @property
    def point(self) -> Point:
        return self._point

    @point.setter
    def point(self, value: Point) -> None:
        self._point = value

    @property
    def truck(self) -> Truck:
        return self._truck

    @truck.setter
    def truck(self, value: Truck) -> None:
        self._truck = value
