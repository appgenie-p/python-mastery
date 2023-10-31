import reader
from stock import Stock
from tools import get_path

port = reader.read_csv_as_dicts("Data/portfolio.csv", [str, int, float])

port = reader.read_csv_as_instances("Data/portfolio.csv", Stock)


