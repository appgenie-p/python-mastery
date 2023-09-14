import csv
from typing import Any, TypeAlias

Path: TypeAlias = str
DictFormat: TypeAlias = list[Any]


def read_csv_as_dicts(file: Path, format: DictFormat) -> list[dict[str, Any]]:
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


def main():
    import tracemalloc

    tracemalloc.start()
    from sys import intern

    rows = read_csv_as_dicts("Data/ctabus.csv", [intern, intern, str, int])
    routeids = {id(row["route"]) for row in rows}
    print(len(routeids))
    print(tracemalloc.get_traced_memory())


if __name__ == "__main__":
    main()
