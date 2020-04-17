from asyncio import gather
from datetime import date
from itertools import chain
from itertools import dropwhile
from itertools import takewhile
from os import PathLike
from pathlib import Path
from typing import Iterable
from typing import Iterator
from typing import Tuple
from typing import Union
from typing import overload

from isoweek import Week

from . import Record
from . import record_date
from . import weeks
from .client import Client
from .archive import Archive
from .archive import Records
from .report import Report
from .report import Section

Result = Union[Records, Tuple[Records, ...]]


def filter_before(records: Iterable[Record], end: date) -> Iterator[Record]:
    return takewhile(lambda record: record_date(record) <= end, records)


def filter_after(records: Iterable[Record], start: date) -> Iterator[Record]:
    return dropwhile(lambda record: record_date(record) < start, records)


def slice_dates(reports: Iterable[Record], start: date, end: date) -> Iterator[Record]:
    return filter_after(filter_before(reports, end), start)


def merge(reports: Iterable[Iterable[Record]], start: date, end: date) -> Records:
    return list(slice_dates(chain.from_iterable(reports), start, end))


class Repository(PathLike):
    root: Path
    report: Report

    def __init__(self, report: Report, root=Path.home() / '.mpr'):
        self.report = report
        self.root = root
        path = Path(self)

        if not root.exists():
            root.mkdir()

        if not path.exists():
            path.mkdir()

    def __fspath__(self) -> str:
        return str(self.root / self.report.slug)

    async def get(self, client: Client, end: date) -> Archive:
        end = min(date.today(), end)
        week = Week.withdate(end)
        archive = Archive(Path(self), week)
        day = archive.day

        if day == 6 or day == end.isoweekday():
            return archive

        records = await client.fetch(week.day(day), end)
        archive.save(records, end)
        return archive

    @overload
    async def query(self, start: date, end: date, __section: Section) -> Records: ...

    @overload
    async def query(self, start: date, end: date, __section: Section, *others: Section) -> Result: ...

    async def query(self, start: date, end: date, section: Section, *others: Section) -> Result:
        sections = (section, *others)

        async with Client(self.report) as client:
            archives = (self.get(client, min(week.saturday(), end)) for week in weeks(start, end))
            reports = (report.get(*sections) for report in await gather(*archives))

        if len(sections) > 1:
            return tuple(merge(report, start, end) for report in zip(*reports))
        else:
            return merge(reports, start, end)
