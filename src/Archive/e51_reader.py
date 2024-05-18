import csv
from typing import (
    Callable,
    Iterable,
    Iterator,
    Optional,
    Sequence,
    Type,
    TypeVar,
    cast,
)

from e37_reader import T


def read_csv_as_dicts(
    filename: str, types: Sequence[Callable], *, headers=None
) -> list[dict]:
    with open(filename) as file:
        return csv_as_dicts(file, types=types, headers=headers)


def read_csv_as_instances(filename: str, cls: Type, *, headers=None) -> list:
    with open(filename) as file:
        records = csv_as_instances(file, cls=cls, headers=headers)
    return records


def csv_as_dicts(
    lines: Iterator,
    types: Sequence[Callable],
    *,
    headers: Optional[Sequence] = None
) -> list[dict]:
    records = []
    if headers is None:
        headers = next(lines)
    headers = cast(Sequence, headers)
    for line in lines:
        record = {
            name: func(val) for name, func, val in zip(headers, types, line)
        }
        records.append(record)
    return records


def csv_as_instances(
    lines: Iterator, cls: Type[T], *, headers=None
) -> list[T]:
    records = []
    _ = next(lines)
    for row in lines:
        record = cls.from_row(row)
        records.append(record)
    return records
