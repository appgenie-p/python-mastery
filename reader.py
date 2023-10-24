import csv
from typing import Any, Protocol, Sequence, Type, TypeAlias, TypeVar

Path: TypeAlias = str
Formats: TypeAlias = Sequence[Any]


class Row:
    def __init__(self, route, date, daytype, numrides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.numrides = numrides

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))


def read_csv_as_dicts(file: Path, format: Formats) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with open(file) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            list_items = [type_(item) for type_, item in zip(format, row)]
            dict_entry = dict(zip(headings, list_items))
            records.append(dict_entry)
    return records


T = TypeVar("T", bound="FromRowProtocol")


class FromRowProtocol(Protocol):
    @classmethod
    def from_row(cls: Type[T], row: Sequence[str]) -> T:
        ...


def read_csv_as_instances(filename: str, cls: Type[T]) -> list[T]:
    records: list[T] = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)
        records.extend(cls.from_row(row) for row in rows)
    return records
