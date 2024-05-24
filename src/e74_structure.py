# e74_structure.py

from abc import ABC
from typing import Any

from e74_validate import (
    PositiveFloat,
    PositiveInteger,
    String,
    Validator,
    validated,
)


class Structure(ABC):
    _fields = ()
    _types = ()

    @classmethod
    def create_init(cls):
        fields = ", ".join(cls._fields)
        init = f"def __init__(self, {fields}):"
        for field in cls._fields:
            init += f"\n    self.{field} = {field}"
        exec(init, globals(), locals())
        cls.__init__ = locals()["__init__"]

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self._fields or __name.startswith("_"):
            return super().__setattr__(__name, __value)
        raise AttributeError(f"No attribute {__name}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}{tuple(self.__dict__.values())}"

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)

    @classmethod
    def from_row(cls, row):
        rowdata = [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)


def validate_attributes(cls):
    """
    Examines the class body for instances of Validators and fills in
    the `_fields` variable.
    """
    validators = []

    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
        elif callable(val) and val.__annotations__:
            setattr(cls, name, validated(val))

    cls._fields = tuple([v.name for v in validators])
    cls._types = tuple([v.expected_type for v in validators])

    if cls._fields:
        cls.create_init()

    return cls


def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls


if __name__ == "__main__":
    Stock = typed_structure(
        "Stock", name=String(), shares=PositiveInteger(), price=PositiveFloat()
    )

    s = Stock("GOOG", 100, 490.1)

    assert s.name == "GOOG"
