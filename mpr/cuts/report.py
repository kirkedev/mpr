from collections import Iterator
from datetime import date
from typing import Tuple

from .cut_type import CutType
from .cut_type import cut_types
from .model import Cut
from .model import parse_record
from ..data.report import Section
from ..data.report import DailyReport
from ..data.repository import Repository


class CutsReport(DailyReport[Cut]):
    class Section(Section):
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

    cuts: Tuple[CutType, ...]

    def __init__(self, *cuts: CutType):
        super().__init__('lm_pk602', 'National Daily Pork - Negotiated Sales - Afternoon', 15)
        self.cuts = cuts

    async def fetch(self, start: date, end: date) -> Iterator[Cut]:
        cuts = self.cuts
        end = min(self.latest, end)
        sections = (self.Section(key) for key, value in cut_types.items() if value in cuts)
        data = await Repository(self).query(start, end, *sections)

        return map(parse_record, data)
