from abc import ABC, abstractmethod
from typing import Any, Optional, Sequence, Type, TypeVar, reveal_type

T = TypeVar("T", bound="TableFormatter")


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


class ColumnFormatMixin:
    formats: Sequence[str] = []

    def row(self, rowdata: Sequence[str]):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


def print_table(
    records: Sequence[object], fields: Sequence[str], formatter: Any
) -> None:
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


def create_formatter(
    format: str,
    *,
    column_formats: Optional[Sequence[str]] = None,
    upper_headers: bool = False,
) -> TableFormatter:
    formatter_cls: Type[TableFormatter]
    match format:
        case "text":
            formatter_cls = TextTableFormatter
        case "csv":
            formatter_cls = CSVTableFormatter
        case "html":
            formatter_cls = HTMLTableFormatter
        case _:
            raise ValueError(f"Unknown table format {format}")

    if column_formats:
        cf = column_formats

        class CFormatterClass(ColumnFormatMixin, formatter_cls):   # type: ignore
            formats = cf

        formatter_cls = CFormatterClass

    if upper_headers:

        class HFormatterClass(UpperHeadersMixin, formatter_cls):  # type: ignore
            pass

        formatter_cls = HFormatterClass

    return formatter_cls()
