
class Point:
    def __init__(self, x: int, y: int, stock_amount: int):
        self._x = x
        self._y = y
        self._stock_amount = stock_amount

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
    def stock_amount(self) -> int:
        return self._stock_amount

    @stock_amount.setter
    def stock_amount(self, value: int) -> None:
        self._stock_amount = value

