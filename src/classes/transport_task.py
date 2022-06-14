
class TransportTask:
    def __init__(self, trucks: list, points: list):
        self._trucks = trucks
        self._points = points

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
