import os

import pytest

from e72_logcall import logformat, logged
from e72_validate import Integer, enforce, validated


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


def test_decor_meta(capsys):
    @logged
    def add(x, y):
        "Adds two things"
        return x + y

    # Проверка, что строка документации сохраняется
    assert add.__doc__ == "Adds two things"

    # Вызов функции и захват её вывода
    add(1, 2)
    captured = capsys.readouterr()

    # Проверка вывода при вызове функции
    assert "Calling add" in captured.out


def test_logormat(capsys):
    @logformat("{func.__code__.co_filename}:{func.__name__}")
    def mul(x, y):
        return x * y

    current_file = os.path.basename(__file__)

    mul(2, 3)
    captured = capsys.readouterr()

    assert f"{current_file}:mul" in captured.out


def test_decorator_for_class_methods(capsys):
    class Spam:
        @logged
        def instance_method(self):
            pass

        @logged
        @classmethod
        def class_method(cls):
            pass

        @logged
        @staticmethod
        def static_method():
            pass

        @logged
        @property
        def property_method(self):
            pass

    s = Spam()
    cap = capsys.readouterr()

    s.instance_method()
    assert "instance_method" in cap.out

    Spam.class_method()
    assert "class_method" in cap.out

    s.property_method
    assert "property_method" in cap.out


def test_enforce_add_success():
    @enforce(x=Integer, y=Integer, return_=Integer)
    def add(x, y):
        return x + y

    r = add(2, 3)

    assert r == 5


def test_enforce_add_failure():
    @enforce(x=Integer, y=Integer, return_=Integer)
    def add(x, y):
        return x + y

    with pytest.raises(TypeError):
        r = add("2", "3")
