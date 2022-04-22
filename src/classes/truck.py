


class Truck():

    def __init__(self, colour: str, location: tuple) -> None:
        self.cargo_amount=0
        self.total_time=0
        self.total_distance=0
        self.colour=colour
        self.location=location
        self.capacity = 1000 if self.colour == 'green' else (1500 if self.colour == 'blue' else  (2000 if 'red' else None))
        self.speed = 1.5 if self.colour == 'green' else (1 if self.colour == 'blue' else (0.75 if 'red' else None))
        self.load_speed = 1 if self.colour == 'green' else (2 if self.colour == 'blue' else (3 if 'red' else None))
        self.unload_speed=4

    @property
    def cargo_amount(self) -> int:
        return self._cargo_amount

    @cargo_amount.setter
    def cargo_amount(self, value: int) -> None:
        self._cargo_amount = value

    @property
    def total_time(self) -> int:
        return self._total_time

    @total_time.setter
    def total_time(self, value: int) -> None:
        self._total_time = value

    @property
    def total_distance(self) -> int:
        return self._total_distance

    @total_distance.setter
    def total_distance(self, value: int) -> None:
        self._total_distance = value

    @property
    def colour(self) -> str:
        return self._colour

    @colour.setter
    def colour(self, value: str) -> None:
        self._colour = value

    @property
    def load_speed(self) -> int:
        return self._load_speed

    @load_speed.setter
    def load_speed(self, value: int) -> None:
        self._load_speed = value

    @property
    def unload_speed(self) -> int:
        return self._unload_speed

    @unload_speed.setter
    def unload_speed(self, value: int) -> None:
        self._unload_speed = value

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, value: float) -> None:
        self._speed = value


    def __str__(self) -> str:
        return f"""
        Car
            Colour: {self.colour}
            Cargo: {self.cargo_amount} / {self.capacity} kg
            Location: {self.location}
            Total Time: {self.total_time} s
            Total distance  {self.total_distance} km 

         """
