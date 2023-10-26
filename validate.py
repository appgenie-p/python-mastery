from typing import Any, NamedTuple, Sequence, Sized, Type


class Validator:
    @classmethod
    def check(cls, value: Any) -> Any:
        return value


class Typed(Validator):
    expected_type = object

    @classmethod
    def check(cls, value: Any):
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
    def check(cls, value: int | float):
        if value < 0:
            raise ValueError("Expected >= 0")
        return super().check(value)


class NonEmpty(Validator):
    @classmethod
    def check(cls, value: Sized):
        if len(value) == 0:
            raise ValueError("Must be non-empty")
        return super().check(value)


class PositiveInteger(Integer, Positive):
    pass


class PositiveFloat(Float, Positive):
    pass


class NonEmptyString(String, NonEmpty):
    pass


class RowFormat(NamedTuple):
    name: Any
    shares: Any
    price: Any


class Stock:
    __slots__ = ("name", "_shares", "_price")
    _types = RowFormat(name=str, shares=int, price=float)

    def __init__(self, name: str, shares: int, price: Any) -> None:
        self.name = name
        self._shares = shares
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: Any) -> None:
        self._price = PositiveFloat.check(value=value)

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, value: Any) -> None:
        self._shares = PositiveInteger.check(value=value)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares: int):
        self.shares -= shares

    @classmethod
    def from_row(cls: Type["Stock"], row: Sequence[str]) -> "Stock":
        return cls(*(func(item) for func, item in zip(cls._types, row)))

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}({self.name!r}, {self.shares!r}, "
            f"{self.price!r})"
        )

    def __eq__(self, other: Any):
        return isinstance(other, Stock) and (
            (self.name, self.shares, self.price)
            == (other.name, other.shares, other.price)
        )
