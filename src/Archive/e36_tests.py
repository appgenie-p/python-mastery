from decimal import Decimal

import pytest

from e33_reader import read_csv_as_instances
from e36_stock import DStock, Stock
from tools import get_path


@pytest.fixture
def portfolio() -> list[Stock]:
    return read_csv_as_instances(get_path("Data/portfolio.csv"), Stock)


def test_from_row():
    row = ["AA", "100", "32.20"]

    sut = Stock.from_row(row)

    assert sut.name == "AA"
    assert sut.shares == 100
    assert sut.price == 32.2
    assert sut.cost == 3220.0000000000005


def test_from_row_inherited():
    row = ["AA", "100", "32.20"]

    sut = DStock.from_row(row)

    assert sut.price == Decimal("32.20")
    assert sut.cost == Decimal("3220.0")


def test_properties_validation():
    sut = Stock("GOOG", 100, 490.10)

    sut.shares = 50
    sut.price = 123.45

    assert sut.shares == 50  # OK
    with pytest.raises(TypeError):
        sut.shares = "50"
    with pytest.raises(ValueError):
        sut.shares = -10
    assert sut.price == 123.45  # OK
    with pytest.raises(TypeError):
        sut.price = "123.45"
    with pytest.raises(ValueError):
        sut.price = -10.0


def test_slots_addition():
    s = Stock("GOOG", 100, 490.10)
    with pytest.raises(AttributeError):
        s.spam = 42


def test_types_read_from_types():
    sut = DStock("AA", 50, Decimal("91.1"))

    with pytest.raises(TypeError):
        sut.price = 92.3


def test_class_repr():
    goog = Stock("GOOG", 100, 490.10)
    assert repr(goog) == "Stock('GOOG', 100, 490.1)"


from io import StringIO

from e36_stock import redirect_stdout


def test_redirect_stdout():
    out_file = StringIO()

    with redirect_stdout(out_file):
        print("Hello, world!")

    assert out_file.getvalue() == "Hello, world!\n"
