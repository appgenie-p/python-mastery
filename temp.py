import tracemalloc
tracemalloc.start()
from sys import intern
import reader
rows = reader.read_csv_as_dicts('Data/ctabus.csv', [intern, str, str, int])
routeids = { id(row['route']) for row in rows }
len(routeids)