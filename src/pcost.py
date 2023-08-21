from dataclasses import dataclass


PATH_TO_FILE = "Data/portfolio.dat"


@dataclass
class Stock:
    name: str
    shares_count: int
    price: float


def read_file():
    with open(PATH_TO_FILE) as f:
        for line in f:
            name, shares_count, price = line.split()
            yield Stock(name, int(shares_count), float(price))