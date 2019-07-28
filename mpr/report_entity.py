from abc import ABC

from tables import Table

from mpr import db
from .observation import Observation
from .observation import Record
from .reports import Report
from .reports import Section


class ReportEntity(Observation[Record], ABC):
    report: Report
    section: Section

    def __init__(self, report: Report, section: Section):
        self.report = report
        self.section = section

    @property
    def table(self) -> Table:
        return db.get(self.report, self.section)
