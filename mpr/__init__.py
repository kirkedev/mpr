from typing import Tuple
from typing import Union

import pandas as pd
from pandas import DataFrame
from pandas import Series

from .cutout.report import CutoutReport
from .purchase.report import PurchaseReport
from .slaughter.report import SlaughterReport

pd.options.display.float_format = '{:,.2f}'.format


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
