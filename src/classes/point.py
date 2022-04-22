
class Point:
    def __init__(self, location: tuple, magazine: bool, cargo_amount: int) -> None:
        self.location = location
        self.magazine = magazine
        self.status = 'active' if self.magazine is False else 'magazine'
        self.cargo_amount = cargo_amount if self.magazine is False else 0

    @property
    def location(self) -> int:
        return self._location

    @location.setter
    def location(self, value: int) -> None:
        self._location = value

    @property
    def magazine(self) -> int:
        return self._magazine

    @magazine.setter
    def magazine(self, value: int) -> None:
        self._magazine = value

    @property
    def status(self) -> int:
        return self._status

    @status.setter
    def status(self, value: int) -> None:
        self._status = value

    @property
    def cargo_amount(self) -> int:
        return self._cargo_amount

    @cargo_amount.setter
    def cargo_amount(self, value: int) -> None:
        self._cargo_amount = value

    def __str__(self) -> str:
        return f""" 
            {'Magazine' if self.magazine == True else 'Point'}
                Location: {self.location}
                Order: {self.cargo_amount} kg
            """


"""
    @property
    def cargo_type(self) -> str:
        return self._cargo_type

    @cargo_type.setter
    def cargo_type(self, value: str) -> None:
        self._cargo_type = value
"""
