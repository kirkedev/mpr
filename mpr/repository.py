import json
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

from isoweek import Week

from mpr.api import Attributes
from mpr.report import Report
from mpr.report import Section

Data = Dict[Section, List[Attributes]]
Result = Tuple[Week, Optional[Data]]


def filepath(location: Path, week: Week) -> Path:
    return location / f"{week}.zip"


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

        with ZipFile(filepath(self.location, week)) as archive:
            if len(sections) == 0:
                sections = map(lambda name: Path(name).stem, archive.namelist())

            return {section: json.loads(archive.read(f"{section}.json")) for section in sections}

    def save(self, week: Week, data: Data):
        with ZipFile(filepath(self.location, week), 'w', ZIP_DEFLATED) as archive:
            for section, values in data.items():
                archive.writestr(f"{section}.json", json.dumps(values))
