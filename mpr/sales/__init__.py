from asyncio import gather
from datetime import date
from itertools import chain
from typing import Iterator

from .cut import Cut
from .cut import report_sections
from .model import Sales
from .model import parse_record
from .report import lm_pk602
from .report import lm_pk610
from .report import lm_pk620
from ..data import weeks
from ..data.repository import Repository


async def daily(start: date, end: date, *cuts: Cut) -> Iterator[Sales]:
    end = min(end, lm_pk602.latest)
    sales = await Repository(lm_pk602).query(start, end, *report_sections(*cuts))

    return map(parse_record, sales)


async def weekly_negotiated(start: date, end: date, *cuts: Cut) -> Iterator[Sales]:
    sections = list(report_sections(*cuts))

    archives = await gather(*(Repository(lm_pk610).get(week.saturday()) for week in weeks(start, end)
        if week.day(lm_pk610.weekday) < lm_pk610.latest))

    return map(parse_record, chain.from_iterable(archive.get(*sections) for archive in archives))


async def weekly_formula(start: date, end: date, *cuts: Cut) -> Iterator[Sales]:
    sections = list(report_sections(*cuts))
    report_weeks = (week + 1 for week in weeks(start, end))

    archives = await gather(*(Repository(lm_pk620).get(week.saturday()) for week in report_weeks
        if week.day(lm_pk620.weekday) < lm_pk620.latest))

    return map(parse_record, chain.from_iterable(archive.get(*sections) for archive in archives))
