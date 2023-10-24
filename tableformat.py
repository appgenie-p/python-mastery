from abc import ABC, abstractmethod
from typing import Any, Sequence

from e34_stock import Stock


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers: Any) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata: Any) -> Any:
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers: Sequence[str]):
        print(" ".join("%10s" % h for h in headers))
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata: Sequence[Any]):
        print(" ".join("%10s" % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers: Sequence[str]):
        print(",".join(headers))

    def row(self, rowdata: Sequence[Any]):
        print(",".join(str(item) for item in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers: Sequence[str]):
        self._form_and_print("<th>{}</th>", headers)

    def row(self, rowdata: Sequence[Any]):
        self._form_and_print("<td>{}</td>", rowdata)

    def _form_and_print(self, inner_tag: str, data: Sequence[Any]) -> None:
        outer = "<tr> {} </tr>"
        inner = inner_tag
        inner_out = " ".join(inner.format(header) for header in data)
        print(outer.format(inner_out))


def print_table(
    records: Sequence[Stock], fields: Sequence[str], formatter: TableFormatter
):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


def create_formatter(format: str) -> TableFormatter:
    match format:
        case "text":
            return TextTableFormatter()
        case "csv":
            return CSVTableFormatter()
        case "html":
            return HTMLTableFormatter()
        case _:
            raise ValueError(f"Unknown table format {format}")
