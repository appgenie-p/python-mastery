from e31_stock import Stock


def test_stock():
    s = Stock("GOOG", 100, 490.10)
    assert s.shares == 100
    s.sell(25)
    assert s.shares == 75
