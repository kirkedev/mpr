from datetime import date
from datetime import timedelta
from functools import singledispatch
from pandas import DataFrame

from ..slaughter import get_slaughter
from .report import cash_index_report


@singledispatch
async def get_cash_prices(start: date, end=date.today()) -> DataFrame:
    slaughter = await get_slaughter(start - timedelta(days=5), end)
    return cash_index_report(slaughter)[start:]


@get_cash_prices.register(int)
async def get_recent_cash_prices(n: int) -> DataFrame:
    today = date.today()
    cash_prices = await get_cash_prices(today - timedelta(n + 10), today)
    return cash_prices.tail(n)
