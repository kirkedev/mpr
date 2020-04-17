import json
from datetime import date
from itertools import chain
from itertools import groupby
from itertools import tee
from operator import itemgetter
from os import PathLike
from pathlib import Path
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Tuple
from typing import Union
from typing import overload
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile

from isoweek import Week

from . import Record
from . import record_date
from .report import Section

Records = List[Record]
Result = Union[Records, Tuple[Records, ...], Dict[str, Records]]


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


def sort_records(records: Iterable[Record]) -> Records:
    return sorted(records, key=itemgetter('label', 'report_date'))


def to_dict(records: Records) -> Dict[str, Records]:
    return {section: list(values) for section, values in groupby(records, key=itemgetter('label'))}


class Archive(PathLike):
    root: Path
    week: Week
    day: int

    def __init__(self, root: Path, week: Week):
        self.root = root
        self.week = week

        matches = list(root.glob(f"{week}D0[0-6].zip"))
        self.day = 0 if len(matches) == 0 else int(matches[0].stem[-1])

    def __fspath__(self) -> str:
        return str(self.root / f"{self.week}D0{self.day}.zip")

    @overload
    def get(self) -> Dict[str, Records]: ...

    @overload
    def get(self, __section: Section) -> Records: ...

    @overload
    def get(self, *sections: Section) -> Result: ...

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
        peek, records = tee(records)
        first = next(peek, None)

        if first is None:
            return

        path = Path(self)

        if path.exists():
            records = chain(*self.get().values(), records)
            path.unlink()

        data = sort_records(records)
        last = record_date(data[-1]).isoweekday()
        self.day = last if last < 5 and end.isoweekday() < 6 else 6

        with ZipFile(self, 'w', ZIP_DEFLATED) as archive:
            for section, values in to_dict(data).items():
                archive.writestr(f"{normalize_path(section)}.json", json.dumps(values, separators=(',', ':')))
