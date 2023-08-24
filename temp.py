from readrides import read_rides_as_dicts

rides = read_rides_as_dicts("Data/ctabus.csv")

print(f"Number of bus routes: {len(set(ride['route'] for ride in rides))}")