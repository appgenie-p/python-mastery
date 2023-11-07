import sys
from abc import ABC
from typing import Any


class Structure(ABC):
    _fields: tuple

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop("self")
        for name, val in locs.items():
            setattr(self, name, val)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self._fields or __name.startswith("_"):
            return super().__setattr__(__name, __value)
        raise AttributeError(f"No attribute {__name}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}{tuple(self.__dict__.values())}"


class Stock(Structure):
    _fields = ("name", "shares", "price")


class Date(Structure):
    _fields = ("year", "month", "day")


# if __name__ == "__main__":
#     s = Stock("GOOG", 100, 490.1)
#     help(Stock)
