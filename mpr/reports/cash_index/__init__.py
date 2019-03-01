from datetime import date
from functools import singledispatch
from pandas import DataFrame

from mpr.api.slaughter import fetch_slaughter
from ..calendar import recent_report_dates
from .report import cash_index_report


@singledispatch
async def get_cash_prices(start: date, end=date.today()) -> DataFrame:
    slaughter = await fetch_slaughter(start, end)
    return cash_index_report(slaughter)


@get_cash_prices.register(int)
async def get_recent_cash_prices(n: int) -> DataFrame:
    first, *_, last = recent_report_dates(n + 3)
    cash_prices = await get_cash_prices(first, last)
    return cash_prices.tail(n)
