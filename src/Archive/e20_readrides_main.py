from e20_readrides import read_rides, read_rides_as_dicts

from e20_readrides_save_methods import (
    save_as_class,
    save_as_class_slots,
    save_as_dataclass,
    save_as_dict,
    save_as_named_tuple,
    save_as_tuple,
)


def main():
    import tracemalloc

    tracemalloc.start()

    methods = [
        save_as_tuple,
        save_as_dict,
        save_as_class,
        save_as_named_tuple,
        save_as_class_slots,
        save_as_dataclass,
    ]

    for method in methods:
        read_rides("Data/ctabus.csv", method)
        current, peak = tracemalloc.get_traced_memory()
        print(
            f"current: {current:,}, peak: {peak:,}, method: {method.__name__}"
        )
        tracemalloc.clear_traces()

    read_rides_as_dicts("Data/ctabus.csv")
    current, peak = tracemalloc.get_traced_memory()
    print(f"current: {current:,}, peak: {peak:,}, method: read_rides_as_dicts")
    tracemalloc.clear_traces()


if __name__ == "__main__":
    main()
