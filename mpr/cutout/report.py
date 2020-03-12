from datetime import date
from itertools import starmap
from typing import Iterator

from .model import Cutout
from .model import parse_record
from ..data.report import DailyReport
from ..data.report import Section
from ..data.repository import Repository


class CutoutReport(DailyReport[Cutout]):
    class Section(Section):
        CUTOUT = 'Cutout and Primal Values'
        DAILY_CHANGE = 'Change From Prior Day'
        FIVE_DAY_AVERAGE = '5-Day Average Cutout and Primal Values'
        VOLUME = 'Current Volume'
        LOIN = 'Loin Cuts'
        BUTT = 'Butt Cuts'
        PICNIC = 'Picnic Cuts'
        HAM = 'Ham Cuts'
        BELLY = 'Belly Cuts'
        RIB = 'Sparerib Cuts'
        JOWL = 'Jowl Cuts'
        TRIM = 'Trim Cuts'
        VARIETY = 'Variety Cuts'
        ADDED_INGREDIENT = 'Added Ingredient Cuts'

    async def get(self, start: date, end: date) -> Iterator[Cutout]:
        end = min(self.latest, end)
        cutout, volume = await Repository(self).query(start, end, self.Section.CUTOUT, self.Section.VOLUME)
        return starmap(parse_record, zip(cutout, volume))
