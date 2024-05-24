# e76_validate.py

import decimal
from functools import wraps
from inspect import Signature, signature
from typing import Any, Callable


class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)

    validators = {}

    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls


class Typed(Validator):
    expected_type = object

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f"Expected {cls.expected_type}")
        return super().check(value)


# class Integer(Typed):
#     expected_type = int


# class Float(Typed):
#     expected_type = float


# class String(Typed):
#     expected_type = str


_typed_classes = [
    ("Integer", int),
    ("Float", float),
    ("Complex", complex),
    ("Decimal", decimal.Decimal),
    ("List", list),
    ("Bool", bool),
    ("String", str),
]

globals().update(
    (name, type(name, (Typed,), {"expected_type": ty}))
    for name, ty in _typed_classes
)


class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError("Must be >= 0")
        return super().check(value)


class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError("Must be non-empty")
        return super().check(value)


class PositiveInteger(Integer, Positive):
    pass


class PositiveFloat(Float, Positive):
    pass


class NonEmptyString(String, NonEmpty):
    pass


def validated(func):
    sig: Signature = signature(func)
    annotations: dict = func.__annotations__
    return_annotation = annotations.pop("return", None)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        errors = []
        for key, value in annotations.items():
            try:
                value.check(bound.arguments[key])
            except Exception as e:
                errors.append(f"    {key}: {e}")

        if errors:
            raise TypeError("Bad Arguments\n" + "\n".join(errors))

        result = func(*args, **kwargs)

        if return_annotation:
            try:
                return_annotation.check(result)
            except Exception as e:
                raise TypeError(f"Bad return value: {e}") from e

        return result

    return wrapper


def enforce(**kwargs):
    annotations: dict = kwargs
    return_annotation = annotations.pop("return_", None)

    def decorator(func):
        sig: Signature = signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            errors = []
            for key, value in annotations.items():
                try:
                    value.check(bound.arguments[key])
                except Exception as e:
                    errors.append(f"    {key}: {e}")

            if errors:
                raise TypeError("Bad Arguments\n" + "\n".join(errors))

            result = func(*args, **kwargs)

            if return_annotation:
                try:
                    return_annotation.check(result)
                except Exception as e:
                    raise TypeError(f"Bad return value: {e}") from e

            return result

        return wrapper

    return decorator


if __name__ == "__main__":
    pass
