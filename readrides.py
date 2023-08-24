import csv
from dataclasses import dataclass
from typing import Any, Callable, NamedTuple, Tuple

Raw = Tuple[str, str, str, int]


class Row:
    def __init__(self, *args: Raw) -> None:
        self.route = args[0]
        self.date = args[1]
        self.daytype = args[2]
        self.rides = args[3]


class RowSlots:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, *args: Raw) -> None:
        self.route = args[0]
        self.date = args[1]
        self.daytype = args[2]
        self.rides = args[3]


class RowNamedTuple(NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int


@dataclass(slots=True)
class RowDataClass:
    route: str
    date: str
    daytype: str
    rides: int


def save_as_class(*args: Raw):
    return Row(*args)


def save_as_class_slots(*args: Raw) -> RowSlots:
    return RowSlots(*args)


def save_as_dataclass(*args: *Raw) -> RowDataClass:
    return RowDataClass(*args)


def save_as_tuple(*args: Raw):
    return args


def save_as_dict(*args: Raw):
    record = {
        "route": args[0],
        "date": args[1],
        "daytype": args[2],
        "rides": args[3],
    }
    return record


def save_as_named_tuple(*args: *Raw):
    return RowNamedTuple(*args)


def read_rides(filename: str, save_method: Callable[..., Any]) -> list[Any]:
    records: list[Raw] = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            records.append(save_method(route, date, daytype, rides))
    return records


def read_rides_as_dicts(path: str) -> list[dict[str, Any]]:
    return read_rides(path, save_as_dict)


def main():
    import tracemalloc

    tracemalloc.start()

    methods = [
        save_as_tuple,
        save_as_dict,
        save_as_class,
        save_as_named_tuple,
        save_as_class_slots,
        save_as_dataclass,
    ]

    for method in methods:
        read_rides("Data/ctabus.csv", method)
        current, peak = tracemalloc.get_traced_memory()
        print(
            f"current: {current:,}, peak: {peak:,}, method: {method.__name__}"
        )
        tracemalloc.clear_traces()


if __name__ == "__main__":
    main()
