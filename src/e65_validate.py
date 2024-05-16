from inspect import Signature, signature
from typing import Any, Callable


class Validator:
    @classmethod
    def check(cls, value):
        return value


class Typed(Validator):
    expected_type = object

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f"Expected {cls.expected_type}")
        return super().check(value)


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


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


class ValidatedFunction:
    def __init__(self, func: Callable) -> None:
        self.func = func
        self.sig: Signature = signature(func)
        self.annotations: dict = func.__annotations__
        self.return_annotation = self.annotations.pop("return", None)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        bound = self.sig.bind(*args, **kwds)

        for key, value in self.annotations.items():
            value.check(bound.arguments[key])

        result = self.func(*args, **kwds)
        if self.return_annotation:
            self.return_annotation.check(result)

        return result
