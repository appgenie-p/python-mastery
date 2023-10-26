import reader
from src.tools import get_path
from stock import Stock
from tableformat import print_table

portfolio = reader.read_csv_as_instances(get_path("Data/portfolio.csv"), Stock)


from tableformat import create_formatter

formatter = create_formatter("csv", column_formats=['"%s"', "%d", "%0.2f"])

print_table(portfolio, ["name", "shares", "price"], formatter)

formatter = create_formatter("text", upper_headers=True)

print_table(portfolio, ["name", "shares", "price"], formatter)
