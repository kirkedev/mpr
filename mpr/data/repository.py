from asyncio import gather
from datetime import date
from itertools import chain
from itertools import dropwhile
from itertools import takewhile
from os import PathLike
from pathlib import Path
from re import search
from typing import Dict
from typing import List
from typing import Iterator
from typing import Optional

from isoweek import Week
from . import record_date

from ..date import weeks
from ..report import Report
from ..report import Section

from .api import fetch
from .api import Record
from .archive import Archive
from .archive import Records
from .archive import Result


def find_archive(path: Path, week: Week) -> Optional[Archive]:
    matches = list(path.glob(f"{week}D0[0-9].zip"))

    if len(matches) == 0:
        return None

    week, day = search(r'(\d{4}W\d{2})D0(\d)', matches[0].stem).groups()
    return Archive(path, Week.fromstring(week), int(day))


def filter_before(records: Iterator[Record], end: date) -> Iterator[Record]:
    return takewhile(lambda record: record_date(record) <= end, records)


def filter_after(records: Iterator[Record], start: date) -> Iterator[Record]:
    return dropwhile(lambda record: record_date(record) < start, records)


def slice_dates(reports: Iterator[List[Record]], start: date, end: date) -> Records:
    first, *middle, last = reports
    return list(chain(filter_after(first, start), *middle, filter_before(last, end)))


def slice_reports(reports: Iterator[Dict[str, Result]], start: date, end: date) -> Dict[str, Records]:
    first, *middle, last = reports
    result = {section: list(filter_after(values, start)) for section, values in first.items()}

    for report in middle:
        for section, values in report.items():
            result[section] += values

    for section, values in last.items():
        result[section] += filter_before(values, end)

    return result


class Repository(PathLike):
    root: Path
    report: Report

    def __init__(self, report: Report, root=Path("data")):
        self.report = report
        self.root = root
        path = Path(self)

        if not root.exists():
            root.mkdir()

        if not path.exists():
            path.mkdir()

    def __fspath__(self) -> str:
        return str(self.root / self.report.slug)

    async def get(self, week: Week, end: date) -> Archive:
        today = date.today()
        end = min(week.saturday(), today, end)
        archive = find_archive(Path(self), week)

        if archive is None:
            records = await fetch(self.report, week.monday(), end)
            return Archive.create(Path(self), week, end, records)

        day = archive.day

        if day == 6 or day == end.isoweekday():
            return archive

        records = list(await fetch(self.report, week.day(day), end))

        if len(records) > 0:
            archive.update(end, records)

        return archive

    async def query(self, start: date, end: date, *sections: Section) -> Result:
        archives = await gather(*(self.get(week, end) for week in weeks(start, end)))
        reports = (report.get(*sections) for report in archives)
        n = len(sections)

        if n == 0:
            return slice_reports(reports, start, end)
        elif n == 1:
            return slice_dates(reports, start, end)
        else:
            return tuple(slice_dates(report, start, end) for report in zip(*reports))
