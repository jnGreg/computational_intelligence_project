
from point import Point
from truck import Truck


class Warehouse(Point):
    def __init__(self, x: int, y: int, stock_amount: int, starting_trucks: list):
        super().__init__(x, y, stock_amount)
        self.starting_trucks = starting_trucks

    @property
    def starting_trucks(self) -> list:
        return self._starting_trucks

    @starting_trucks.setter
    def starting_trucks(self, value: list) -> None:
        self._starting_trucks = value
