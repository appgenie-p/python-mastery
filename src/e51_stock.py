import csv
import sys
from decimal import Decimal
from typing import Any, Generator, NamedTuple, Sequence, Type

from e37_reader import T


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
        return (
            f"{type(self).__name__}({self.name!r}, {self.shares!r}, "
            f"{self.price!r})"
        )

    def __eq__(self, other: Any):
        return isinstance(other, Stock) and (
            (self.name, self.shares, self.price)
            == (other.name, other.shares, other.price)
        )


class DStock(Stock):
    _types = RowFormat(str, int, Decimal)


class redirect_stdout:
    def __init__(self, out_file: Any):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty: Any, val: Any, tb: Any) -> None:
        sys.stdout = self.stdout


def read_portfolio(path: str, cls: Type[T]) -> Generator[T, None, None]:
    with open(path, "rt") as f:
        reader = csv.reader(f)
        _ = next(reader)
        for row in reader:
            yield cls.from_row(row)
