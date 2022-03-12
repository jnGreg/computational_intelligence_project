
from src.classes.point import Point


class Warehouse(Point):
    def __init__(self, x: int, y: int, cargo_amount: int, cargo_type: str):
        super().__init__(x, y, cargo_amount, cargo_type)
