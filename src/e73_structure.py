from abc import ABC
from typing import Any

from e73_validate import Validator
from e73_validate import validated


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


def get_dynamic_init_code(cls):
    fields = ", ".join(cls._fields)
    init_code = f"def __init__(self, {fields}):"
    for field in cls._fields:
        init_code += f"\n    self.{field} = {field}"
    return init_code


if __name__ == "__main__":
    from e73_stock import Stock
    import e73_reader as reader

    s = Stock.from_row(["GOOG", "100", "490.1"])
    port = reader.read_csv_as_instances("../Data/portfolio.csv", Stock)
