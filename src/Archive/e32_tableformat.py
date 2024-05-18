import csv
from dataclasses import dataclass
from typing import Generator, Sequence, TypeAlias

import tools

PATH = tools.get_path("Data/portfolio.csv")


@dataclass
class Stock:
    name: str
    shares: int
    price: float

    def cost(self):
        return self.shares * self.price

    def sell(self, shares: int):
        self.shares -= shares


Portfolio: TypeAlias = Generator[Stock, None, None]


def read_portfolio(path: str) -> Portfolio:
    with open(path, "rt") as f:
        reader = csv.reader(f)
        _ = next(reader)
        for row in reader:
            name, shares, price = row
            yield Stock(name, int(shares), float(price))


def print_table(portfolio: Portfolio, cols: Sequence[str]):
    f = "{:>10}"
    print(" ".join(f.format(attr) for attr in cols))
    for member in portfolio:
        print(" ".join(f"{getattr(member, attr):>10}" for attr in cols))


if __name__ == "__main__":
    portfolio = read_portfolio(PATH)
    print_table(portfolio, ["name", "shares", "price"])
