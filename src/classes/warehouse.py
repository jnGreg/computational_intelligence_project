
from src.classes.point import Point


class Warehouse(Point):
    def __init__(self, x: int, y: int, cargo_amount: int, cargo_type: str, starting_trucks: list):
        super().__init__(x, y, cargo_amount, cargo_type)
        self.starting_trucks = starting_trucks

    @property
    def starting_trucks(self) -> list:
        return self._starting_trucks

    @starting_trucks.setter
    def starting_trucks(self, value: list) -> None:
        self._starting_trucks = value
