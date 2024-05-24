# e76_structure.py

from collections import ChainMap
from typing import Any

from e76_validate import Validator, validated


class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)


class Structure(metaclass=StructureMeta):
    _fields = ()
    _types = ()

    def __setattr__(self, name, value) -> None:
        if name in self._fields or name.startswith("_"):
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}{tuple(self.__dict__.values())}"

    @classmethod
    def from_row(cls, row):
        rowdata = [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)

    @classmethod
    def create_init(cls):
        """
        Create an __init__ method from _fields
        """
        args = ",".join(cls._fields)
        code = f"def __init__(self, {args}):\n"
        for name in cls._fields:
            code += f"    self.{name} = {name}\n"
        locs = {}
        exec(code, locs)
        cls.__init__ = locs["__init__"]

    @classmethod
    def __init_subclass__(cls):
        # Apply the validated decorator to subclasses
        validate_attributes(cls)


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

