from dataclasses import dataclass
from typing import NamedTuple, Sequence

from e20_readrides import Raw


class Row:
    def __init__(self, *args: Raw) -> None:
        self.route = args[0]
        self.date = args[1]
        self.daytype = args[2]
        self.rides = args[3]


class RowSlots:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, *args: Raw) -> None:
        self.route = args[0]
        self.date = args[1]
        self.daytype = args[2]
        self.rides = args[3]


class RowNamedTuple(NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int


@dataclass(slots=True)
class RowDataClass:
    route: str
    date: str
    daytype: str
    rides: int


class RideData(Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        return {
            "route": self.routes[index],
            "date": self.dates[index],
            "daytype": self.daytypes[index],
            "rides": self.numrides[index],
        }

    def append(self, d):
        self.routes.append(d["route"])
        self.dates.append(d["date"])
        self.daytypes.append(d["daytype"])
        self.numrides.append(d["rides"])
