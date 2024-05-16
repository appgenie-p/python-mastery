import pytest

from e65_validate import ValidatedFunction
from validate import Integer


def test_validated_function(capfd):
    def add(x, y):
        return x + y
    add = ValidatedFunction(add)

    result = add(2, 3)
    captured = capfd.readouterr()

    assert result == 5
    assert (
        "Calling <function test_validated_function.<locals>.add at"
        in captured.out
    )


def test_validated_function_with_types():
    def add(x: Integer, y: Integer) -> Integer:
        return x + y
    add = ValidatedFunction(add)

    result = add(2, 3)

    assert result == 5


def test_validated_function_with_type_check_via_annotations_failure():
    def add(x: Integer, y: Integer):
        return x + y
    add = ValidatedFunction(add)

    with pytest.raises(TypeError) as e:
        add("two", "three")
