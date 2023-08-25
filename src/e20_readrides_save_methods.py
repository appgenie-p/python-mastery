from e20_readrides import Raw
from e20_readrides_ds import Row, RowDataClass, RowNamedTuple, RowSlots


def save_as_class(*args: Raw):
    return Row(*args)


def save_as_class_slots(*args: Raw) -> RowSlots:
    return RowSlots(*args)


def save_as_dataclass(*args: *Raw) -> RowDataClass:
    return RowDataClass(*args)


def save_as_tuple(*args: Raw):
    return args


def save_as_dict(*args: Raw):
    return {
        "route": args[0],
        "date": args[1],
        "daytype": args[2],
        "rides": args[3],
    }


def save_as_named_tuple(*args: *Raw):
    return RowNamedTuple(*args)
