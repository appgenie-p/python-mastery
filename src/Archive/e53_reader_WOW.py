import csv
from typing import Callable, Iterator, Sequence, Type

from e37_reader import T


def read_csv_as_dicts(
    filename: str, types: Sequence[Callable], *, headers=None
) -> list[dict]:
    with open(filename) as file:
        return csv_as_dicts(file, types=types, headers=headers)


def read_csv_as_instances(filename: str, cls: Type, *, headers=None) -> list:
    with open(filename) as file:
        return csv_as_instances(file, cls=cls, headers=headers)


def convert_csv(lines: Iterator, converter: Callable, *, headers=None) -> list:
    rows: Iterator[list[str]] = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return [converter(row, headers) for row in rows]


def csv_as_instances(lines: Iterator, cls: Type[T], *, headers=None) -> list:
    return convert_csv(lines, lambda row, headers: cls.from_row(row))


def csv_as_dicts(
    lines: Iterator, types: Sequence[Callable], *, headers=None
) -> list:
    return convert_csv(
        lines,
        lambda row, headers: {
            name: func(val) for name, func, val in zip(headers, types, row)
        },
    )
