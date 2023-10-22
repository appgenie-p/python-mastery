import csv
from decimal import Decimal
from typing import Any, Generator, NamedTuple, Sequence, Type, TypeAlias

from e33_reader import T


class RowFormat(NamedTuple):
    name: Any
    shares: Any
    price: Any


class Stock:
    __slots__ = ("name", "_shares", "_price")
    _types = RowFormat(str, int, float)

    def __init__(self, name: str, shares: int, price: Any) -> None:
        self.name = name
        self._shares = shares
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: Any) -> None:
        if not isinstance(value, self._types.price):
            raise TypeError("Expected float")
        if value < 0:
            raise ValueError("Must be >= 0")
        self._price = value

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, value: Any) -> None:
        if not isinstance(value, self._types.shares):
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
    def from_row(cls: Type["Stock"], row: Sequence[str]) -> "Stock":
        return cls(*(func(item) for func, item in zip(cls._types, row)))

    def __repr__(self) -> str:
        return f"Stock({self.name}, {self.shares}, {self.price})"


class DStock(Stock):
    _types = RowFormat(str, int, Decimal)


def read_portfolio(path: str, cls: Type[T]) -> Generator[T, None, None]:
    with open(path, "rt") as f:
        reader = csv.reader(f)
        _ = next(reader)
        for row in reader:
            yield cls.from_row(row)
