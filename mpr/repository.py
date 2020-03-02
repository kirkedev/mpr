import json
from datetime import date
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

from isoweek import Week

from mpr.api import Attributes
from mpr.date import weeks
from mpr.report import Report
from mpr.report import Section

Data = Dict[str, List[Attributes]]
Result = Tuple[Week, Optional[Data]]


def filepath(location: Path, week: Week) -> Path:
    return location / f"{str(week)}.json.gz"


class Repository:
    location: Path

    def __init__(self, report: Report, location: Path):
        self.location = location / report.name

        if self.location.exists() is False:
            self.location.mkdir()

    def has(self, week: Week) -> bool:
        return filepath(self.location, week).exists()

    def get(self, week: Week, *sections: Section) -> Optional[Data]:
        if self.has(week) is False:
            return None

        with open(str(filepath(self.location, week))) as data:
            result = json.load(data)
            return result if len(sections) == 0 else dict(filter(lambda it: it[0] in sections, result.items()))

    def save(self, week: Week, data: Data):
        with open(str(filepath(self.location, week)), 'x') as location:
            json.dump(data, location)

    def query(self, start: date, end: date) -> Iterator[Result]:
        for week in weeks(start, end):
            yield week, self.get(week)
