from datetime import date
from datetime import datetime
from datetime import time
from typing import Union
from typing import Tuple
from enum import Enum

import pandas as pd
from pytz import timezone
from pandas import Series
from pandas import DataFrame

pd.options.display.float_format = '{:,.2f}'.format


class Report:
    slug: str
    description: str
    hour: int

    def __init__(self, slug: str, description: str, hour: int):
        self.slug = slug
        self.description = description
        self.hour = hour

    def __str__(self):
        return self.slug

    def released(self, end: date) -> bool:
        release = datetime.combine(end, time(self.hour, tzinfo=timezone('America/Chicago')))
        return release < datetime.now(tz=timezone('America/Chicago'))


class Section(str, Enum):
    def __str__(self):
        return self.value


class PurchaseReport(Report):
    class Section(Section):
        VOLUME = 'Current Volume by Purchase Type'
        BARROWS_AND_GILTS = 'Barrows/Gilts (producer/packer sold)'
        CARCASS_MEASUREMENTS = 'Matrix, 185 lb Carcass Basis'
        CARCASS_WEIGHT_DIFF = 'Carcass Weight Differentials'
        AVERAGE_MARKET_HOG = '5-Day Rolling Average Market Hog based on Slaughter Data Submitted'
        SOWS = 'Sows'
        STATES = 'State of Origin'


class SlaughterReport(Report):
    class Section(Section):
        SUMMARY = 'Summary'
        BARROWS_AND_GILTS = 'Barrows/Gilts'
        CARCASS_MEASUREMENTS = 'Carcass Measurements'
        SOWS_AND_BOARS = 'Sows/Boars'
        SCHEDULED_SWINE = '14-Day Scheduled Swine'
        NEGOTIATED_BARROWS_AND_GILTS = 'Barrows/Gilts Negotiated'


class CutoutReport(Report):
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


def normalize_section(section: Union[Section, str]) -> str:
    return section.replace('/', '_')


def denormalize_section(section: Union[Section, str]) -> str:
    return section.replace('_', '/')


def compute_change(values: Series) -> Series:
    return values - values.shift(1)


def with_change(values: Series) -> Tuple[Series, Series]:
    values = values.round(decimals=2)
    return values, compute_change(values)


def create_table(*columns: Union[Series, DataFrame]) -> DataFrame:
    return pd.concat(columns, axis=1)


lm_hg200 = PurchaseReport('lm_hg200', 'Daily Direct Hog Prior Day - Purchased Swine', 8)
lm_hg201 = SlaughterReport('lm_hg201', 'Daily Direct Hog Prior Day - Slaughtered Swine', 10)
lm_hg202 = PurchaseReport('lm_hg202', 'Daily Direct Hog - Morning', 11)
lm_hg203 = PurchaseReport('lm_hg203', 'Daily Direct Hog - Afternoon', 15)
lm_pk600 = CutoutReport('lm_pk600', 'National Daily Pork - Negotiated Sales - Morning', 11)
lm_pk602 = CutoutReport('lm_pk602', 'National Daily Pork - Negotiated Sales - Afternoon', 15)
