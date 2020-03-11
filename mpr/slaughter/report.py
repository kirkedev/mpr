from datetime import date
from typing import Iterator

from .model import Slaughter
from .model import parse_record
from ..data.report import Report
from ..data.report import Section
from ..data.repository import Repository


class SlaughterReport(Report):
    class Section(Section):
        SUMMARY = 'Summary'
        BARROWS_AND_GILTS = 'Barrows/Gilts'
        CARCASS_MEASUREMENTS = 'Carcass Measurements'
        SOWS_AND_BOARS = 'Sows/Boars'
        SCHEDULED_SWINE = '14-Day Scheduled Swine'
        NEGOTIATED_BARROWS_AND_GILTS = 'Barrows/Gilts Negotiated'

    async def fetch(self, start: date, end: date) -> Iterator[Slaughter]:
        slaughter = await Repository(self).query(start, end, self.Section.BARROWS_AND_GILTS)
        return map(parse_record, slaughter)
