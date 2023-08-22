import collections
import heapq
import pprint
from typing import Any

from src.readrides import RowDataClass, read_rides, save_as_dataclass

Raw = RowDataClass

rides: list[Raw] = read_rides("Data/ctabus.csv", save_as_dataclass)


def count_bus_routs() -> int:
    """Count the number of bus routes."""
    return len(set(ride.route for ride in rides))


def count_people_on_date(route: str, date: str) -> int:
    """Count the number of people on a given route on a given date."""
    return sum(
        ride.rides
        for ride in rides
        if ride.route == route and ride.date == date
    )


def count_total_rides_for_each_route() -> dict[str, int]:
    """Count the total number of rides for each route."""
    return {
        route: sum(ride.rides for ride in rides if ride.route == route)
        for route in {ride.route for ride in rides}
    }


def greatest_increase_in_ridership(
    top_routes_count: int = 5, year_range: tuple[int, int] = (2001, 2011)
) -> Any:
    """Return the five bus routes with the greatest increase in ridership."""
    priority_queue = []
    route_total_rides = {}
    counter = collections.Counter()
    for route in {ride.route for ride in rides}:
        for year in range(*year_range):
            route_sum = sum(
                ride.rides
                for ride in rides
                if ride.route == route
                and int(ride.date.split("/")[-1]) == year
            )
            counter[route] += route_sum
        if len(priority_queue) < 5:
            heapq.heappush(priority_queue, route_total_rides[route])
        else:
            heapq.heappushpop(priority_queue, route_total_rides[route])
    return priority_queue


if __name__ == "__main__":
    # print(f"Number of bus routes: {count_bus_routs()}")
    # print(
    #     f"Number of people on route 22 on 2011-02-02: "
    #     f"{count_people_on_date('22', '02/02/2011')}"
    # )
    # pprint.pprint(
    #     f"Total rides for each route: {count_total_rides_for_each_route()}"
    # )
    pprint.pprint(greatest_increase_in_ridership())
