import csv
from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Generator,
    Iterable,
    Protocol,
    Sequence,
    Type,
    TypeAlias,
)

import tools

PATH = tools.get_path("Data/portfolio.csv")


@dataclass
class Stock:
    types: ClassVar[tuple[Type[Any], ...]] = (str, int, float)
    name: str
    shares: int
    price: float

    def cost(self):
        return self.shares * self.price

    def sell(self, shares: int):
        self.shares -= shares

    @classmethod
    def from_row(cls, row: Iterable[str]):
        return cls(*(func(item) for func, item in zip(cls.types, row)))


Portfolio: TypeAlias = Generator[Stock, None, None]


from decimal import Decimal


class DStock(Stock):
    types = (str, int, Decimal)
