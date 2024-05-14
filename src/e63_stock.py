from e63_structure import Structure


class Stock(Structure):
    def __init__(self, name, shares, price):
        super().set_fields()
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


if __name__ == "__main__":
    s = Stock(name="GOOG", shares=100, price=490.1)
