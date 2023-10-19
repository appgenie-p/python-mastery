from dataclasses import dataclass
from typing import Iterable, TypeAlias

import tools

PATH = tools.get_path("Data/portfolio.csv")


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


Portfolio: TypeAlias = Iterable[Stock]


def read_portfolio(path: str) -> Portfolio:
    with open(path, "rt") as f:
        _ = f.readline()
        for line in f:
            name, shares, price = line.split(",")
            yield Stock(name, int(shares), float(price))


def print_portfolio(portfolio: Portfolio) -> None:
    print("{:>10} {:>10} {:>10s}".format("name", "shares", "price"))
    print(("-" * 10 + " ") * 2 + "-" * 10)
    for s in portfolio:
        print("%10s %10d %10.2f" % (s.name.strip('"'), s.shares, s.price))


if __name__ == "__main__":
    portfolio = read_portfolio(PATH)
    print_portfolio(portfolio)
