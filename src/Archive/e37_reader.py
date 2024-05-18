import csv
from typing import Any, Generic, Protocol, Sequence, Type, TypeAlias, TypeVar

Path: TypeAlias = str
Types: TypeAlias = Sequence[Type[Any]]

from abc import ABC, abstractmethod

Row: TypeAlias = Sequence[str]


T = TypeVar("T", bound="FromRowProtocol")


class FromRowProtocol(Protocol):
    @classmethod
    def from_row(cls: Type[T], row: Sequence[str]) -> T:
        ...


class CSVParser(ABC):
    def parse(self, filename: str) -> list[Any]:
        records: list[Any] = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers: Row, row: Row) -> Any:
        pass


class DictCSVParser(CSVParser):
    def __init__(self, types: Types) -> None:
        self.types = types

    def make_record(self, headers: Row, row: Row) -> dict[str, Any]:
        return {
            name: func(val)
            for name, func, val in zip(headers, self.types, row)
        }


class InstanceCSVParser(CSVParser, Generic[T]):
    def __init__(self, cls: Type[T]):
        self.cls = cls

    def make_record(self, headers: Row, row: Row) -> T:
        return self.cls.from_row(row)


def read_csv_as_instances(filename: str, cls: Type[T]) -> list[T]:
    formatter = InstanceCSVParser(cls)
    return formatter.parse(filename)


def read_csv_as_dicts(file: Path, format: Types) -> list[dict[str, Any]]:
    formatter = DictCSVParser(format)
    return formatter.parse(file)
