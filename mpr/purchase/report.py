from typing import Iterator

from pandas import DataFrame

from mpr.purchase import Purchase


def purchase_report(records: Iterator[Purchase]) -> DataFrame:
    return DataFrame()
