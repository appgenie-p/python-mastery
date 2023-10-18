from dataclasses import dataclass
from typing import Iterable


@dataclass
class Stock:
    name: str
    shares: int
    price: float

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares: int):
        self.shares -= shares


def read_portfolio(path: str) -> Iterable[Stock]:
    with open(path, "rt") as f:
        _ = f.readline()
        for line in f:
            name, shares, price = line.split(",")
            yield Stock(name, int(shares), float(price))
