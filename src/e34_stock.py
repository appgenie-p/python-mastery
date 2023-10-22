import csv
from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Generator,
    Iterable,
    NamedTuple,
    Type,
    TypeAlias,
)

import tools
from e33_reader import T

PATH = tools.get_path("Data/portfolio.csv")


class RowFormat(NamedTuple):
    name: Type[str]
    shares: Any
    price: Any


@dataclass(slots=True)
class Stock:
    _types: ClassVar[NamedTuple] = RowFormat(str, int, float)
    name: str
    _shares: int
    _price: float

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self.__class__._types.price):
            raise TypeError("Expected float")
        if value < 0:
            raise ValueError("Must be >= 0")
        self._price = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self.__class__._types.shares):
            raise TypeError("Expected int")
        if value < 0:
            raise ValueError("Must be >= 0")
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares: int):
        self.shares -= shares

    @classmethod
    def from_row(cls, row: Iterable[str]):
        return cls(*(func(item) for func, item in zip(cls._types, row)))


from decimal import Decimal


class DStock(Stock):
    _types = RowFormat(str, int, Decimal)


Portfolio: TypeAlias = Generator[Stock, None, None]


def read_portfolio(path: str, cls: Type[T]) -> Generator[T, None, None]:
    with open(path, "rt") as f:
        reader = csv.reader(f)
        _ = next(reader)
        for row in reader:
            yield cls.from_row(row)
