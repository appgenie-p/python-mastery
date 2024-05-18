def typedproperty(expected_type):
    private_name = "name very private"

    def __set_name__(self, attr, name):
        private_name = name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f"Expected {expected_type}")
        setattr(self, private_name, val)

    return value


def Float():
    return typedproperty(float)


def Integer():
    return typedproperty(int)


def String():
    return typedproperty(str)


if __name__ == "__main__":

    class Stock:
        name = String()
        shares = Integer()
        price = Float()

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    s = Stock("AA", 3, 44.4)
    print(s.name, s.price, s.shares)