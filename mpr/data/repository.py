from asyncio import gather
from datetime import date
from datetime import datetime
from itertools import chain
from itertools import dropwhile
from itertools import groupby
from itertools import takewhile
from operator import itemgetter
from os import PathLike
from pathlib import Path
from typing import Dict
from typing import List
from typing import Iterator

from isoweek import Week

from ..date import weeks
from ..report import Report
from ..report import Section

from .api import fetch
from .api import Attributes
from .archive import Archive
from .archive import Data
from .archive import Result

date_format = "%m/%d/%Y"


def parse_date(date_string: str) -> date:
    return datetime.strptime(date_string, date_format).date()


def filter_before(records: Iterator[Attributes], end: date) -> Iterator[Attributes]:
    return takewhile(lambda record: parse_date(record['report_date']) <= end, records)


def filter_after(records: Iterator[Attributes], start: date) -> Iterator[Attributes]:
    return dropwhile(lambda record: parse_date(record['report_date']) < start, records)


def slice_dates(reports: Iterator[List[Attributes]], start: date, end: date) -> Data:
    first, *middle, last = reports
    return list(chain(filter_after(first, start), *middle, filter_before(last, end)))


def slice_reports(reports: Iterator[Dict[str, Result]], start: date, end: date) -> Dict[str, Data]:
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

    def __init__(self, report: Report, root=Path("mpr/data")):
        self.report = report
        self.root = root

        path = Path(self)

        if not path.exists():
            path.mkdir()

    def __fspath__(self) -> str:
        return str(self.root / self.report.slug)

    async def get(self, week: Week) -> Archive:
        archive = Archive(Path(self), week)

        if not Path(archive).exists():
            attributes = await fetch(self.report, week.monday(), week.sunday())
            data = sorted(attributes, key=itemgetter('label', 'report_date'))
            archive.save({section: list(values) for section, values in groupby(data, key=itemgetter('label'))})

        return archive

    async def query(self, start: date, end: date, *sections: Section) -> Result:
        archives = await gather(*(self.get(week) for week in weeks(start, end)))
        reports = (report.get(*sections) for report in archives)
        n = len(sections)

        if n == 0:
            return slice_reports(reports, start, end)
        elif n == 1:
            return slice_dates(reports, start, end)
        else:
            return tuple(slice_dates(report, start, end) for report in zip(*reports))
