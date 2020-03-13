from asyncio import gather
from datetime import date
from itertools import chain
from itertools import dropwhile
from itertools import takewhile
from operator import methodcaller
from os import PathLike
from pathlib import Path
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import overload

from isoweek import Week

from . import record_date
from . import weeks
from .api import Client
from .api import Record
from .archive import Archive
from .archive import Records
from .archive import Result
from .report import Report
from .report import Section


def filter_before(records: Iterable[Record], end: date) -> Iterator[Record]:
    return takewhile(lambda record: record_date(record) <= end, records)


def filter_after(records: Iterable[Record], start: date) -> Iterator[Record]:
    return dropwhile(lambda record: record_date(record) < start, records)


def slice_dates(reports: Iterable[Record], start: date, end: date) -> Iterator[Record]:
    return filter_after(filter_before(reports, end), start)


def merge(reports: Iterable[Iterable[Record]], start: date, end: date) -> Records:
    return list(slice_dates(chain.from_iterable(reports), start, end))


def update_section(result: Dict[str, Iterable[Record]], section: str, values: Iterable[Record]):
    if section not in result:
        result[section] = list(values)
    else:
        result[section] += values


def merge_reports(reports: Iterable[Dict[str, Records]], start: date, end: date) -> Dict[str, Records]:
    first, *others = reports

    if len(others) == 0:
        return {section: list(slice_dates(values, start, end)) for section, values in first.items()}

    result = {section: list(filter_after(values, start)) for section, values in first.items()}

    if len(others) == 1:
        last = others[0]
    else:
        *middle, last = others

        for section, values in chain.from_iterable(map(methodcaller('items'), middle)):
            update_section(result, section, values)

    for section, values in last.items():
        update_section(result, section, filter_before(values, end))

    return result


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
    async def query(self, start: date, end: date) -> Dict[str, Records]: ...

    @overload
    async def query(self, start: date, end: date, __section: Section) -> Records: ...

    @overload
    async def query(self, start: date, end: date, *sections: Section) -> Result: ...

    async def query(self, start: date, end: date, *sections: Section) -> Result:
        async with Client(self.report) as client:
            archives = (self.get(client, min(week.saturday(), end)) for week in weeks(start, end))
            reports = (report.get(*sections) for report in await gather(*archives))

        n = len(sections)

        if n == 0:
            return merge_reports(reports, start, end)
        elif n == 1:
            return merge(reports, start, end)
        else:
            return tuple(merge(report, start, end) for report in zip(*reports))
