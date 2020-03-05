import json
from os import PathLike
from pathlib import Path
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile

from isoweek import Week

from ..report import Section
from .api import Attributes

Data = List[Attributes]
Result = Union[Data, Tuple[Data], Dict[str, Data]]


def get_section(archive: ZipFile, section: Section) -> Data:
    return json.loads(archive.read(f"{section}.json"))


def get_sections(archive: ZipFile, *sections: Section) -> Tuple[Data, ...]:
    return tuple(json.loads(archive.read(f"{section}.json")) for section in sections)


def get_report(archive: ZipFile) -> Dict[str, Data]:
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

    def get(self, *sections: Section) -> Result:
        n = len(sections)

        with ZipFile(self) as archive:
            if n == 0:
                return get_report(archive)
            elif n == 1:
                return get_section(archive, sections[0])
            else:
                return get_sections(archive, *sections)

    def save(self, data: Dict[str, Data]):
        with ZipFile(self, 'w', ZIP_DEFLATED) as archive:
            for section, values in data.items():
                archive.writestr(f"{section}.json", json.dumps(values, separators=(',', ':')))
