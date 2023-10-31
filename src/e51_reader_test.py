import e51_reader as reader
import e51_stock as stock
import gzip
file = gzip.open('Data/portfolio.csv.gz')
port = reader.csv_as_instances(file, stock.Stock)
port
# [Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44),
#  Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1),
#  Stock('IBM', 100, 70.44)]
