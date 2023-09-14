import csv
from typing import Any, TypeAlias


class DataCollection:
    def __init__(self, headings):
        [setattr(self, heading, []) for heading in headings]

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


Path: TypeAlias = str
DictFormat: TypeAlias = list[Any]


def read_csv_as_columns(file: Path, *, types: DictFormat) -> DataCollection:
    """
    Read the bus ride data as a list of columns
    """
    with open(file) as f:
        rows = csv.reader(f)
        headings = next(rows)
        dc = DataCollection(headings)
        for row in rows:
            list_items = [type_(item) for type_, item in zip(types, row)]
            zip(headings, list_items)
            [
                getattr(dc, heading).append(item)
                for heading, item in zip(headings, list_items)
            ]
    return dc


def main():
    data = read_csv_as_columns("Data/ctabus.csv", types=[str, str, str, int])
    print(data)
    print(len(data))
    print(data[0], "/n", data[1], "/n", data[2])


if __name__ == "__main__":
    main()