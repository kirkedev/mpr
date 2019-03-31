from datetime import date
from functools import singledispatch
from pandas import DataFrame

from ..calendar import recent_report_dates
from ..cutout.api import pk602

from .report import cutout_report


@singledispatch
async def get_cutout(start: date, end=date.today()) -> DataFrame:
    cutout = await pk602(start, end)
    return cutout_report(cutout)


@get_cutout.register(int)
async def get_recent_cash_prices(n: int) -> DataFrame:
    first, *_, last = recent_report_dates(n + 8)
    cutout = await get_cutout(first, last)
    return cutout.tail(n)
