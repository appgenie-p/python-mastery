from e64_structure import Structure


class Stock(Structure):
    _fields = ("name", "shares", "price")

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


Stock.create_init()


if __name__ == "__main__":
    s = Stock(name="GOOG", shares=100, price=490.1)
