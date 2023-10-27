import reader
from src.tools import get_path

PATH = get_path("Data/portfolio.csv")


file = open(PATH)
port = reader.csv_as_dicts(file, [str, int, float])
port