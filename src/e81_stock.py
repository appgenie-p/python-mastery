# e81_stock.py

from e81_structure import Structure


class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares


if __name__ == "__main__":
    s = Stock(name="GOOG", shares=100, price=490.1)
    s.name = 50
    pass
