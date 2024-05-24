# e74_structure_tests.py

from e74_structure import typed_structure
from e74_validate import PositiveFloat, PositiveInteger, String


def test_typed_structure():
    Stock = typed_structure(
        "Stock", name=String(), shares=PositiveInteger(), price=PositiveFloat()
    )

    s = Stock("GOOG", 100, 490.1)

    assert s.name == 'GOOG'