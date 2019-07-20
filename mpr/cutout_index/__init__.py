from datetime import date
from datetime import timedelta
from functools import singledispatch
from pandas import DataFrame

from ..cutout.api import pk602

from .report import cutout_report


@singledispatch
async def get_cutout_index(start: date, end=date.today()) -> DataFrame:
    cutout = await pk602(start, end)
    return cutout_report(cutout)


@get_cutout_index.register(int)
async def get_recent_cash_prices(n: int) -> DataFrame:
    today = date.today()
    cutout = await get_cutout_index(today - timedelta(days=n + 12), today)
    return cutout.tail(n)
