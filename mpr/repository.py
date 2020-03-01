from abc import ABC
from datetime import date
from pathlib import Path
from typing import Generic
from typing import TypeVar
from typing import NamedTuple

from mpr.reports import Report

Record = TypeVar('Record', bound=NamedTuple)


class Repository(Generic[Record], ABC):
    location: Path
    report: Report

    def __init__(self, location: Path, report: Report):
        self.location = location
        self.report = report

    def query(self, start: date, end: date):
        raise NotImplementedError

    def ingest(self, month: int, year: int):
        raise NotImplementedError
