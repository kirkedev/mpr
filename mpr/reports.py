from typing import Union
from typing import Tuple
from enum import Enum

import pandas as pd
from pandas import Series
from pandas import DataFrame

pd.options.display.float_format = '{:,.2f}'.format


class Report(Enum):
    @property
    def name(self):
        return self._name_.lower()

    def __getattr__(self, item):
        if item != '_value_':
            return getattr(self.value, item).value

        raise AttributeError


class PurchaseReport(Report):
    LM_HG200 = 'Daily Direct Hog Prior Day - Purchased Swine'
    LM_HG202 = 'Daily Direct Hog - Morning'
    LM_HG203 = 'Daily Direct Hog - Afternoon'

    class Section(Report):
        # VOLUME = 'Current Volume by Purchase Type'
        BARROWS_AND_GILTS = 'Barrows/Gilts (producer/packer sold)'
        # CARCASS_MEASUREMENTS = 'Matrix, 185 lb Carcass Basis'
        # CARCASS_WEIGHT_DIFF = 'Carcass Weight Differentials'
        # AVERAGE_MARKET_HOG = '5-Day Rolling Average Market Hog based on Slaughter Data Submitted'
        # SOWS = 'Sows'
        # STATES = 'State of Origin'


class SlaughterReport(Report):
    LM_HG201 = 'Daily Direct Hog Prior Day - Slaughtered Swine'

    class Section(Report):
        # SUMMARY = 'Summary'
        BARROWS_AND_GILTS = 'Barrows/Gilts'
        # CARCASS_MEASUREMENTS = 'Carcass Measurements'
        # SOWS_AND_BOARS = 'Sows/Boars'
        # SCHEDULED_SWINE = '14-Day Scheduled Swine'
        # NEGOTIATED_BARROWS_AND_GILTS = 'Barrows/Gilts Negotiated'


class CutoutReport(Report):
    LM_PK600 = 'National Daily Pork - Negotiated Sales - Morning'
    LM_PK602 = 'National Daily Pork - Negotiated Sales - Afternoon'

    class Section(Report):
        CUTOUT = 'Cutout and Primal Values'
        # DAILY_CHANGE = 'Change From Prior Day'
        # FIVE_DAY_AVERAGE = '5-Day Average Cutout and Primal Values'
        VOLUME = 'Current Volume'
        # LOIN = 'Loin Cuts'
        # BUTT = 'Butt Cuts'
        # PICNIC = 'Picnic Cuts'
        # HAM = 'Ham Cuts'
        # BELLY = 'Belly Cuts'
        # RIB = 'Sparerib Cuts'
        # JOWL = 'Jowl Cuts'
        # TRIM = 'Trim Cuts'
        # VARIETY = 'Variety Cuts'
        # ADDED_INGREDIENT = 'Added Ingredient Cuts'


def compute_change(values: Series) -> Series:
    return values - values.shift(1)


def with_change(values: Series) -> Tuple[Series, Series]:
    values = values.round(decimals=2)
    return values, compute_change(values)


def create_table(*columns: Union[Series, DataFrame]) -> DataFrame:
    return pd.concat(columns, axis=1)
