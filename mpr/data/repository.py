from asyncio import gather
from datetime import date
from datetime import datetime
from itertools import chain
from itertools import groupby
from operator import itemgetter
from os import PathLike
from pathlib import Path
from typing import List
from typing import Iterator

from isoweek import Week

from ..date import weeks
from ..report import Report
from ..report import Section

from .api import fetch
from .api import Attributes
from .archive import Archive

date_format = "%m/%d/%Y"


def parse_date(date_string: str) -> date:
    return datetime.strptime(date_string, date_format).date()


def slice_dates(reports: Iterator[List[Attributes]], start: date, end: date) -> List[Attributes]:
    first, *middle, last = reports

    return list(chain(
        (record for record in first if parse_date(record['report_date']) >= start),
        *middle,
        (record for record in last if parse_date(record['report_date']) <= end)
    ))


class Repository(PathLike):
    root: Path
    report: Report

    def __init__(self, report: Report, root=Path("data")):
        self.report = report
        self.root = root

        path = Path(self)

        if not path.exists():
            path.mkdir()

    def __fspath__(self) -> str:
        return str(self.root / self.report.name)

    async def get(self, week: Week) -> Archive:
        archive = Archive(Path(self), week)

        if not Path(archive).exists():
            attributes = await fetch(self.report, week.monday(), week.sunday())
            data = sorted(attributes, key=itemgetter('label', 'report_date'))
            archive.save({section: list(values) for section, values in groupby(data, key=itemgetter('label'))})

        return archive

    async def query(self, start: date, end: date, *sections: Section):
        n = len(sections)
        archives = await gather(*(self.get(week) for week in weeks(start, end)))
        reports = (report.get(*sections) for report in archives)

        if n == 0:
            return {section: slice_dates(report, start, end) for section, report in reports}
        elif n == 1:
            return slice_dates(reports, start, end)
        else:
            return tuple(slice_dates(report, start, end) for report in zip(*reports))
