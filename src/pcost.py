from dataclasses import dataclass
from typing import Any, Generator


@dataclass
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
    print(StocksInfo("Data/portfolio3.dat").portfolio_cost())
