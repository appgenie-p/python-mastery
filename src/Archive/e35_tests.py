import pytest

import e33_reader as reader
import e34_stock as stock
import e35_tableformat as tableformat
from tools import get_path


@pytest.fixture
def portfolio() -> list[stock.Stock]:
    return reader.read_csv_as_instances(
        get_path("Data/portfolio.csv"), stock.Stock
    )


def test_formatter_class(portfolio: list[stock.Stock]) -> None:
    formatter = tableformat.TextTableFormatter()
    tableformat.print_table(portfolio, ["name", "shares", "price"], formatter)


def test_csv_formatter(
    portfolio: list[stock.Stock], capfd: pytest.CaptureFixture[str]
):
    formatter = tableformat.CSVTableFormatter()
    expected_stdout = """name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
"""

    tableformat.print_table(portfolio, ["name", "shares", "price"], formatter)

    assert capfd.readouterr().out == expected_stdout


def test_html_formatter(
    portfolio: list[stock.Stock], capfd: pytest.CaptureFixture[str]
):
    formatter = tableformat.HTMLTableFormatter()
    expected_out = """<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
"""

    tableformat.print_table(portfolio, ["name", "shares", "price"], formatter)

    assert capfd.readouterr().out == expected_out


def test_formatter_factory(
    portfolio: list[stock.Stock], capfd: pytest.CaptureFixture[str]
):
    formatter = tableformat.create_formatter("html")
    expected_out = """<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
"""

    tableformat.print_table(portfolio, ["name", "shares", "price"], formatter)

    assert capfd.readouterr().out == expected_out
