import csv
from typing import (
    Any,
    Callable,
    Iterable,
    Protocol,
    Sequence,
    Type,
    TypeAlias,
    TypeVar,
)

T = TypeVar("T", bound="FromRowProtocol")

RowOfStr: TypeAlias = Sequence[str]


class FromRowProtocol(Protocol):
    @classmethod
    def from_row(cls: Type[T], row: RowOfStr) -> T:
        ...


Types: TypeAlias = Sequence[Callable]


def read_csv_as_dicts(filename, types: Types) -> list[dict]:
    """
    Read CSV data into a list of dictionaries with optional type conversion
    """
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = {
                name: func(val) for name, func, val in zip(headers, types, row)
            }
            records.append(record)
    return records


def read_csv_as_instances(filename, cls: Type[T]) -> list[T]:
    """
    Read CSV data into a list of instances
    """
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records


def csv_as_dicts(lines: Iterable[str], types: Types) -> list[dict]:
    records = []
    lines_iterator = iter(lines)
    headers = next(lines_iterator).strip().split(",")
    for line in lines:
        record = {
            name: func(val) for name, func, val in zip(headers, types, line.strip().split(","))
        }
        records.append(record)
    return records


def csv_as_instances(lines: Iterable[RowOfStr], cls: Type[T]) -> list[T]:
    records = []
    lines_iterator = iter(lines)
    headers = next(lines_iterator)
    for line in lines:
        record = cls.from_row(line)
        records.append(record)
    return records
