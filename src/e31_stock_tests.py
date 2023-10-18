import tools
from e31_stock import Stock, read_portfolio

PORTFOLIO_PATH = tools.get_path('Data/portfolio.csv')


def test_stock_sell():
    sut = Stock("GOOG", 100, 490.10)

    sut.sell(25)

    assert sut.shares == 75


def test_read_portfolio():
    sut = read_portfolio(PORTFOLIO_PATH)

    stocks = list(sut)

    assert len(stocks) == 7
    assert isinstance(stocks[0], Stock)
