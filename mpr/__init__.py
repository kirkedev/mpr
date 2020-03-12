from typing import Tuple
from typing import Union

import pandas as pd
from pandas import DataFrame
from pandas import Series

pd.options.display.float_format = '{:,.2f}'.format


def compute_change(values: Series) -> Series:
    return values - values.shift(1)


def with_change(values: Series) -> Tuple[Series, Series]:
    values = values.round(decimals=2)
    return values, compute_change(values)


def create_table(*columns: Union[Series, DataFrame]) -> DataFrame:
    return pd.concat(columns, axis=1)
