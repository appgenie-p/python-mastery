import csv
from typing import Any, Callable, NamedTuple, Tuple

records: list[Any] = []

Raw = Tuple[str, str, str, int]


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


def save_as_class(*args: Raw):
    class Row:
        def __init__(self, *args: Raw) -> None:
            self.route = args[0]
            self.date = args[1]
            self.daytype = args[2]
            self.rides = args[3]

    return Row(*args)


def save_as_named_tuple(*args: Raw):
    class Row(NamedTuple):
        route: str
        date: str
        daytype: str
        rides: int

    return Row(*args)


def save_as_class_slots(*args: Raw):
    class Row:
        __slots__ = ["route", "date", "daytype", "rides"]

        def __init__(self, route: str, date: str, daytype: str, rides: int):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    return Row(*args)


def read_rides(filename: str, save_method: Callable[..., Any]) -> list[Raw]:
    records: list[Raw] = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            records.append(save_method(route, date, daytype, rides))
    return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()

    results = [
        read_rides("Data/ctabus.csv", save_as_dict),
        read_rides("Data/ctabus.csv", save_as_tuple),
        # read_rides("Data/ctabus.csv", save_as_named_tuple),
        # read_rides("Data/ctabus.csv", save_as_class),
        # read_rides("Data/ctabus.csv", save_as_class_slots),
    ]

    current, peak = 0, 0

    for result in results:
        current, peak = tracemalloc.get_traced_memory()
        print(current, peak)
        tracemalloc.clear_traces()
