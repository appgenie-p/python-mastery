import csv
import logging
from typing import Callable, Iterator, Sequence, Type

from e37_reader import T

log = logging.getLogger(__name__)


def read_csv_as_dicts(
    filename: str, types: Sequence[Callable], *, headers=None
) -> list[dict]:
    with open(filename) as file:
        return csv_as_dicts(file, types=types, headers=headers)


def read_csv_as_instances(filename: str, cls: Type, *, headers=None) -> list:
    with open(filename) as file:
        return csv_as_instances(file, cls=cls, headers=headers)


def convert_csv(lines: Iterator, converter: Callable, *, headers=None) -> list:
    rows: Iterator[list[str]] = csv.reader(lines)
    res = []
    if headers is None:
        headers = next(rows)
    for row_num, row in enumerate(rows, start=1):
        try:
            res.append(converter(row, headers))
        except ValueError as e:
            msg_warning = f"Row {row_num}: Bad row: {row}"
            msg_debug = f"Row {row_num}: Reason: {e}"
            log.warning(msg_warning)
            log.debug(msg_debug)
            continue
    return res


def csv_as_instances(lines: Iterator, cls: Type[T], *, headers=None) -> list:
    def make_instance(row, headers) -> T:
        return cls.from_row(row)

    return convert_csv(lines, make_instance)


def csv_as_dicts(
    lines: Iterator, types: Sequence[Callable], *, headers=None
) -> list:
    return convert_csv(
        lines,
        lambda row, headers: {
            name: func(val) for name, func, val in zip(headers, types, row)
        },
    )
