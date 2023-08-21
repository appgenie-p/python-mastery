import tracemalloc
f = open('Data/ctabus.csv')
tracemalloc.start()
lines = f.readlines()
len(lines)
current, peak = tracemalloc.get_traced_memory()
print(current)
print(peak)