import json
from itertools import groupby
from operator import itemgetter
from os import PathLike
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

from isoweek import Week

from mpr.api import Attributes
from mpr.api import fetch
from mpr.report import Report
from mpr.report import Section

Data = Dict[Section, List[Attributes]]
Result = Tuple[Week, Optional[Data]]


def get_section(archive: ZipFile, section: Section) -> List[Attributes]:
    return json.loads(archive.read(f"{section}.json"))


def get_sections(archive: ZipFile, *sections: Section) -> Tuple[List[Attributes], ...]:
    return tuple(json.loads(archive.read(f"{section}.json")) for section in sections)


def get_report(archive: ZipFile) -> Data:
    sections = (Path(name).stem for name in archive.namelist())
    return {section: json.loads(archive.read(f"{section}.json")) for section in sections}


class Archive(PathLike):
    root: Path
    week: Week

    def __init__(self, root: Path, week: Week):
        self.root = root
        self.week = week

    def __fspath__(self) -> str:
        return str(self.root / str(self.week))

    def get(self, *sections: Section) -> Union[Data, List[Attributes], Tuple[List[Attributes]]]:
        n = len(sections)

        with ZipFile(self) as archive:
            if n == 0:
                return get_report(archive)
            elif n == 1:
                return get_section(archive, sections[0])
            else:
                return get_sections(archive, *sections)

    def save(self, data: Data):
        with ZipFile(self, 'w', ZIP_DEFLATED) as archive:
            for section, values in data.items():
                archive.writestr(f"{section}.json", json.dumps(values))


class Repository(PathLike):
    root: Path
    report: Report

    def __init__(self, report: Report, root=Path("data")):
        self.root = root
        self.report = report
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

    def save(self, week: Week, data: Data):
        return Archive(Path(self), week).save(data)
