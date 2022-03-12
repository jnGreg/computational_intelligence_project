
from warehouse import Warehouse


class Truck:
    def __init__(self, colour: str, capacity: int, load_time: int, unload_time: int,
                 speed: float, start_point: Warehouse):
        self._colour = colour
        self._capacity = capacity
        self._load_time = load_time
        self._unload_time = unload_time
        self._speed = speed
        self._start_point = start_point

    @property
    def colour(self) -> str:
        return self._colour

    @colour.setter
    def colour(self, value: str) -> None:
        self._colour = value

    @property
    def load_time(self) -> int:
        return self._unload_time

    @load_time.setter
    def load_time(self, value: int) -> None:
        self._load_time = value

    @property
    def unload_time(self) -> int:
        return self._unload_time

    @unload_time.setter
    def unload_time(self, value: int) -> None:
        self._unload_time = value

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, value: float) -> None:
        self._speed = value

    @property
    def start_point(self) -> Warehouse:
        return self._start_point

    @start_point.setter
    def start_point(self, value: Warehouse) -> None:
        self._start_point = value


