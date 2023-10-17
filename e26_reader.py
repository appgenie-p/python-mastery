import csv
from typing import Any, Sequence, TypeAlias

Path: TypeAlias = str
Formats: TypeAlias = Sequence[Any]


class DataCollection:
    def __init__(self, headings: list[str]):
        for heading in headings:
            setattr(self, heading, [])

    def __len__(self) -> int:
        self.attribute_names = list(vars(self).keys())
        first_attr = getattr(self, self.attribute_names[0])
        return len(first_attr)

    def __getitem__(self, index: int) -> dict[str, Any]:
        attrs = [getattr(self, attr) for attr in self.attribute_names]
        return {
            name: value[index]
            for name, value in zip(self.attribute_names, attrs)
        }


def read_csv_as_columns(file: Path, *, types: Formats) -> DataCollection:
    """Read the bus ride data as a list of columns."""

    with open(file) as f:
        rows = csv.reader(f)
        headings: list[str] = next(rows)
        dc = DataCollection(headings)
        for row in rows:
            list_items = [type_(item) for type_, item in zip(types, row)]
            [
                getattr(dc, heading).append(item)
                for heading, item in zip(headings, list_items)
            ]
    return dc


def read_csv_as_dicts(file: Path, format: Formats) -> list[dict[str, Any]]:
    """
    Read the bus ride data as a list of dicts
    """
    records: list[dict[str, Any]] = []
    with open(file) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            list_items = [type_(item) for type_, item in zip(format, row)]
            dict_entry = dict(zip(headings, list_items))
            records.append(dict_entry)
    return records
