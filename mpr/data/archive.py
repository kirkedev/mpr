import json
from datetime import date
from itertools import chain
from itertools import groupby
from operator import itemgetter
from os import PathLike
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple
from typing import Union
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile

from isoweek import Week

from ..report import Section

from .api import Record
from . import record_date

Records = List[Record]
Result = Union[Records, Tuple[Records], Dict[str, Records]]


def normalize_path(section: str) -> str:
    return section.replace('/', '_')


def denormalize_path(section: str) -> str:
    return section.replace('_', '/')


def get_section(archive: ZipFile, section: str) -> Records:
    return json.loads(archive.read(f"{normalize_path(section)}.json"))


def get_sections(archive: ZipFile, *sections: str) -> Tuple[Records, ...]:
    return tuple(get_section(archive, section) for section in sections)


def get_report(archive: ZipFile) -> Dict[str, Records]:
    sections = list(Path(name).stem for name in archive.namelist())
    return {denormalize_path(section): get_section(archive, section) for section in sections}


def sort_records(records: Iterator[Record]) -> Records:
    return sorted(records, key=itemgetter('label', 'report_date'))


def to_dict(records: Records) -> Dict[str, Records]:
    return {section: list(values) for section, values in groupby(records, key=itemgetter('label'))}


class Archive(PathLike):
    root: Path
    week: Week
    day: int

    @classmethod
    def create(cls, root: Path, end: date, records: Iterator[Record]) -> 'Archive':
        archive = cls(root, Week.withdate(end))
        archive.save(records, end)
        return archive

    def __init__(self, root: Path, week: Week):
        self.root = root
        self.week = week

        matches = list(root.glob(f"{week}D0[0-6].zip"))

        if len(matches) == 0:
            self.day = 0
        else:
            self.day = int(matches[0].stem[-1])

    def __fspath__(self) -> str:
        return str(self.root / f"{self.week}D0{self.day}.zip")

    def get(self, *sections: Section) -> Result:
        n = len(sections)

        with ZipFile(self) as archive:
            if n == 0:
                return get_report(archive)
            elif n == 1:
                return get_section(archive, sections[0])
            else:
                return get_sections(archive, *sections)

    def save(self, records: Iterator[Record], end: date):
        records = sort_records(records)
        last = record_date(records[-1]).isoweekday()
        self.day = last if last < 5 and end.isoweekday() < 6 else 6

        with ZipFile(self, 'w', ZIP_DEFLATED) as archive:
            for section, values in to_dict(records).items():
                archive.writestr(f"{normalize_path(section)}.json", json.dumps(values, separators=(',', ':')))

    def update(self, end: date, records: Iterator[Record]):
        data = chain(*self.get().values(), records)
        Path(self).unlink()
        self.save(data, end)
