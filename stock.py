import csv
import sys
from decimal import Decimal
from typing import Any, Generator, NamedTuple, Sequence, Type

from reader import T
from validate import PositiveFloat, PositiveInteger, String


class RowFormat(NamedTuple):
    name: Any
    shares: Any
    price: Any


class Stock:
    _types = RowFormat(str, int, float)
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name: str, shares: int, price: Any) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self) -> float:
        return self.shares * self.price  # type: ignore

    def sell(self, shares: int) -> None:
        self.shares -= shares  # type: ignore

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
