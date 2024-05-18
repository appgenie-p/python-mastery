import pytest

import tools
from e31_stock import Stock, print_portfolio, read_portfolio

PATH = tools.get_path("Data/portfolio.csv")


def test_stock_sell():
    sut = Stock("GOOG", 100, 490.10)

    sut.sell(25)

    assert sut.shares == 75


def test_read_portfolio():
    sut = read_portfolio(PATH)

    stocks = list(sut)

    assert len(stocks) == 7
    assert isinstance(stocks[0], Stock)


def test_print_portfolio(capfd: pytest.CaptureFixture[str]):
    portfolio = read_portfolio(PATH)
    eo = """      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
"""

    print_portfolio(portfolio)
    captured = capfd.readouterr()

    assert captured.out == eo
