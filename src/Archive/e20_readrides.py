import csv
from typing import Any, Callable

from e20_readrides_ds import RideData

Raw = tuple[str, str, str, int]


class RidesRides:
    def __init__(self, save_method: Callable[..., Any]) -> None:
        self.records: list = []
        self.save_method = save_method

    def read_rides(self, filepath: str):
        with open(filepath, "r") as f:
            rows = csv.reader(f)
            self._skip_header(rows)
            self._generate_record(rows)
        return self.records

    def _skip_header(self, rows):
        _ = next(rows)

    def _generate_record(self, rows):
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            self.records.append(self.save_method(route, date, daytype, rides))


def read_rides_as_columns(filename):
    """
    Read the bus ride data into 4 lists, representing columns
    """
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(
        routes=routes, dates=dates, daytypes=daytypes, numrides=numrides
    )


def read_rides_as_dicts(filename):
    """
    Read the bus ride data as a list of dicts
    """
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                "route": route,
                "date": date,
                "daytype": daytype,
                "rides": rides,
            }
            records.append(record)
    return records
