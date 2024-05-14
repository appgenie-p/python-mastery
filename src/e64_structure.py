from abc import ABC
from typing import Any


class Structure(ABC):
    _fields = ()

    @classmethod
    def create_init(cls):
        pass

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self._fields or __name.startswith("_"):
            return super().__setattr__(__name, __value)
        raise AttributeError(f"No attribute {__name}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}{tuple(self.__dict__.values())}"


if __name__ == "__main__":
    from e64_stock import Stock
    s = Stock("GOOG", 100, 490.1)
    print(repr(s))
