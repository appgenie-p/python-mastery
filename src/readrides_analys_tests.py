from dataclasses import dataclass

from readrides_analys import greatest_increase_in_ridership


@dataclass
class Ride:
    date: str
    route: str
    rides: int


def test_greatest_increase_in_ridership():
    rides = [
        Ride(date="01/01/2001", route="A", rides=100),
        Ride(date="01/01/2001", route="B", rides=200),
        Ride(date="01/01/2001", route="C", rides=300),
        Ride(date="01/01/2001", route="D", rides=400),
        Ride(date="01/01/2001", route="E", rides=500),
        Ride(date="01/01/2011", route="A", rides=200),
        Ride(date="01/01/2011", route="B", rides=400),
        Ride(date="01/01/2011", route="C", rides=600),
        Ride(date="01/01/2011", route="D", rides=800),
        Ride(date="01/01/2011", route="E", rides=1000),
    ]
    expected_result = [
        ("E", 1500),
        ("D", 1200),
        ("C", 900),
        ("B", 600),
        ("A", 300),
    ]
    assert (
        greatest_increase_in_ridership(5, (2001, 2011), rides)
        == expected_result
    )
