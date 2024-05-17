import pytest

from e71_validate import Integer, validated


def test_valigated_add_success():
    @validated
    def add(x: Integer, y: Integer) -> Integer:
        return x + y

    r = add(2, 3)

    assert r == 5


def test_valigated_add_failure():
    @validated
    def add(x: Integer, y: Integer) -> Integer:
        return x + y

    with pytest.raises(TypeError):
        r = add("2", "3")


def test_valigated_pow_success():
    @validated
    def pow(x: Integer, y: Integer) -> Integer:
        return x**y

    r = pow(2, 3)

    assert r == 8


def test_valigated_pow_failure():
    @validated
    def pow(x: Integer, y: Integer) -> Integer:
        return x**y

    with pytest.raises(TypeError):
        r = pow(2, -1)


def test_validated_with_method():
    class Stock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

        @property
        def cost(self):
            return self.shares * self.price

        @validated
        def sell(self, nshares: Integer):
            self.shares -= nshares

    s = Stock("GOOG", 100, 490.1)

    s.sell(10)

    assert s.shares == 90
