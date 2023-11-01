import pytest

from e61_structure import Stock


def test_class_creation():
    s = Stock("GOOG", 100, 490.1)
    assert s.name == "GOOG"
    assert s.shares == 100
    assert s.price == 490.1
    with pytest.raises(TypeError):
        Stock("AA", 50)


def test_only_defined_attrs_can_be_set():
    sut = Stock("GOOG", 100, 490.1)

    sut.shares = 50
    sut._shares = 100

    with pytest.raises(AttributeError):
        sut.share = 50
    assert sut.shares == 50
    assert sut._shares == 100
