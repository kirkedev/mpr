from datetime import date
from typing import Tuple
from typing import NamedTuple
from typing import Union
from typing import Iterator
from .date import DateInterval

# Load Algorithm...
# given a date range...
#   create a ReportMonth for each month in the request range
#   Retrieve report months from table's fetched attribute that match the requested ReportMonth
#   Find the date difference between each requested report range and the corresponding fetched report range
#   Request the report for those dates and save it into the table
#   Replace the fetched report month with the requested report month in table's fetched attribute

Month = Tuple[int, int]


class ReportMonth(NamedTuple):
    year: int
    month: int
    end: int = None

    @property
    def dates(self) -> DateInterval:
        year = self.year
        month = self.month
        end = self.end
        last = date(year, month, end) if end else min(date(*next_month(year, month), 1), date.today())
        return date(year, month, 1), last

    def __hash__(self) -> int:
        return hash((self.year, self.month))

    def __eq__(self, other) -> bool:
        return isinstance(other, ReportMonth) and hash(self) == hash(other) and self.end == other.end


def next_month(year: int, month: int) -> Month:
    return (year, month + 1) if month < 12 else (year + 1, 1)


def get_months(start: date, end: date) -> Iterator[Month]:
    current = (start.year, start.month)
    last = (end.year, end.month)

    while current <= last:
        yield current
        current = next_month(*current)


def report_months(start: date, end: date) -> Iterator[ReportMonth]:
    return map(lambda it: ReportMonth(*it), get_months(start, end))


def report_diff(requested: ReportMonth, fetched: ReportMonth) -> Union[DateInterval, None]:
    assert requested.month == fetched.month, "Reports must be the same month"

    if requested == fetched:
        return None

    first = fetched.dates[1]
    second = requested.dates[1]
    return min(first, second), max(first, second)
