from datetime import date
from datetime import timedelta
from functools import singledispatch
from pandas import DataFrame

from mpr import cutout
from .report import cutout_report


@singledispatch
async def get_cutout_index(start: date, end=date.today()) -> DataFrame:
    records = await cutout.afternoon(start - timedelta(10), end)
    return cutout_report(records)[start:]


@get_cutout_index.register(int)
async def get_recent_cutout_index(n: int) -> DataFrame:
    today = date.today()
    cutout_index = await get_cutout_index(today - timedelta(days=n + 10), today)
    return cutout_index.tail(n)
