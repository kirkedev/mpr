from datetime import date
from typing import Iterator

from .model import Purchase
from .model import parse_record
from ..data.report import Report
from ..data.report import Section
from ..data.repository import Repository


class PurchaseReport(Report[Purchase]):
    class Section(Section):
        VOLUME = 'Current Volume by Purchase Type'
        BARROWS_AND_GILTS = 'Barrows/Gilts (producer/packer sold)'
        CARCASS_MEASUREMENTS = 'Matrix, 185 lb Carcass Basis'
        CARCASS_WEIGHT_DIFF = 'Carcass Weight Differentials'
        AVERAGE_MARKET_HOG = '5-Day Rolling Average Market Hog based on Slaughter Data Submitted'
        SOWS = 'Sows'
        STATES = 'State of Origin'

    async def fetch(self, start: date, end: date) -> Iterator[Purchase]:
        purchases = await Repository(self).query(start, end, self.Section.BARROWS_AND_GILTS)
        return map(parse_record, purchases)
