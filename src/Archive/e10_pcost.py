from dataclasses import dataclass
from typing import Any, Generator


@dataclass(frozen=True)
class Stock:
    name: str
    shares_count: int
    price: float


class StocksInfo:
    def __init__(self, path: str) -> None:
        self._path = path

    def get_stocks(self) -> Generator[Stock, Any, Any]:
        with open(self._path) as f:
            for line in f:
                name, shares_count, price = line.split()
                try:
                    yield Stock(name, int(shares_count), float(price))
                except ValueError as err:
                    print(f"Couldn't parse: {repr(line)}\n" f"Reason: {err}")

    def portfolio_cost(self) -> float:
        total_cost = 0.0
        for stock in self.get_stocks():
            total_cost += stock.shares_count * stock.price

        return total_cost


if __name__ == "__main__":
    print(StocksInfo("Data/portfolio.dat").portfolio_cost())


"""
total_cost = 0.0

with open('../../Data/portfolio.dat', 'r') as f:
    for line in f:
        fields = line.split()
        nshares = int(fields[1])
        price = float(fields[2])
        total_cost = total_cost + nshares * price

print(total_cost)
"""