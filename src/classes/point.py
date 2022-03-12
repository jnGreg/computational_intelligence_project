
class Point:
    def __init__(self, x: int, y: int, cargo_amount: int, cargo_type: str):
        self._x = x
        self._y = y
        self._cargo_amount = cargo_amount
        self._cargo_type = cargo_type

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        self._y = value

    @property
    def cargo_amount(self) -> int:
        return self._cargo_amount

    @cargo_amount.setter
    def cargo_amount(self, value: int) -> None:
        self._cargo_amount = value

    @property
    def cargo_type(self) -> str:
        return self._cargo_type

    @cargo_type.setter
    def cargo_type(self, value: str) -> None:
        self._cargo_type = value

