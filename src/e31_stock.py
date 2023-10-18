from dataclasses import dataclass


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

