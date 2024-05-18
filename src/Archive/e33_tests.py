from decimal import Decimal

from e33_reader import Row, read_csv_as_instances
from e33_stock import DStock, Stock
from tools import get_path


def test_from_row():
    row = ["AA", "100", "32.20"]

    sut = Stock.from_row(row)

    assert sut.name == "AA"
    assert sut.shares == 100
    assert sut.price == 32.2
    assert sut.cost() == 3220.0000000000005


def test_from_row_inherited():
    row = ["AA", "100", "32.20"]

    sut = DStock.from_row(row)

    assert sut.price == Decimal("32.20")
    assert sut.cost() == Decimal("3220.0")


def test_read_csv_as_instances():
    sut = read_csv_as_instances(get_path("Data/portfolio.csv"), Stock)

    assert len(sut) == 7
    assert all(isinstance(obj, Stock) for obj in sut)


def test_read_csv_as_instances_row():
    sut = read_csv_as_instances(get_path("Data/ctabus.csv"), Row)

    assert len(sut) == 577563
