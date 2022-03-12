
class TransportTask:
    def __init__(self, warehouses: list, trucks: list, points: list):
        self._warehouses = warehouses
        self._trucks = trucks
        self._points = points

    @property
    def warehouses(self) -> list:
        return self._warehouses

    @warehouses.setter
    def warehouses(self, value: list) -> None:
        self._warehouses = value

    @property
    def trucks(self) -> list:
        return self._trucks

    @trucks.setter
    def trucks(self, value: list) -> None:
        self._trucks = value

    @property
    def points(self) -> list:
        return self._points

    @points.setter
    def points(self, value: list) -> None:
        self._points = value
