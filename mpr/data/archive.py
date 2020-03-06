import json
from datetime import date
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
from ..report import normalize_section
from ..report import denormalize_section

from .api import Record
from . import record_date

Records = List[Record]
Result = Union[Records, Tuple[Records], Dict[str, Records]]


def get_section(archive: ZipFile, section: Section) -> Records:
    return json.loads(archive.read(f"{normalize_section(section)}.json"))


def get_sections(archive: ZipFile, *sections: Section) -> Tuple[Records, ...]:
    return tuple(json.loads(archive.read(f"{normalize_section(section)}.json")) for section in sections)


def get_report(archive: ZipFile) -> Dict[str, Records]:
    sections = list(Path(name).stem for name in archive.namelist())
    return {denormalize_section(section): json.loads(archive.read(f"{section}.json")) for section in sections}


def sort_records(records: Iterator[Record]) -> Records:
    return sorted(records, key=itemgetter('label', 'report_date'))


def to_dict(records: Records) -> Dict[str, Records]:
    return {section: list(values) for section, values in groupby(records, key=itemgetter('label'))}


class Archive(PathLike):
    root: Path
    week: Week
    day: int

    @classmethod
    def create(cls, root: Path, week: Week, end: date, records: Iterator[Record]) -> 'Archive':
        data = sort_records(records)
        day = record_date(data[-1]).weekday() if end.weekday() < 5 else 5
        archive = cls(root, week, day)
        archive.save(to_dict(data))
        return archive

    def __init__(self, root: Path, week: Week, day: int):
        self.root = root
        self.week = week
        self.day = day

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

    def save(self, data: Dict[str, Records]):
        with ZipFile(self, 'w', ZIP_DEFLATED) as archive:
            for section, values in data.items():
                archive.writestr(f"{normalize_section(section)}.json", json.dumps(values, separators=(',', ':')))

    def update(self, end: date, records: Iterator[Record]):
        records = sort_records(records)
        day = record_date(records[-1]).weekday() if end.weekday() < 5 else 5
        data = self.get()
        report = to_dict(records)

        for section, values in report.items():
            if section in data:
                data[section] += values
            else:
                data[section] = values

        self.save(data)
        Path(self).rename(Path(self.root) / f"{self.week}D0{day}.zip")
        self.day = day
