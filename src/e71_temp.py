from e71_validate import Integer, validated


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares


s = Stock("GOOG", 100, 490.1)

s.sell(10)

assert s.shares == 90
