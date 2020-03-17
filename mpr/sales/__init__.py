from datetime import date
from typing import Iterator

from isoweek import Week

from .cut import Cut
from .cut import report_sections
from .model import Sales
from .model import parse_record
from .report import lm_pk602
from .report import lm_pk610
from .report import lm_pk620
from ..data.repository import Repository


async def daily(start: date, end: date, *cuts: Cut) -> Iterator[Sales]:
    end = min(end, lm_pk602.latest)
    sales = await Repository(lm_pk602).query(start, end, *report_sections(*cuts))

    return map(parse_record, sales)


async def weekly_negotiated(start: date, end: date, *cuts: Cut) -> Iterator[Sales]:
    first = Week.withdate(start)
    last = Week.withdate(min(date.today(), end))
    start = first.monday()

    if last.day(lm_pk610.weekday) < lm_pk610.latest:
        last -= 1

    return map(parse_record, await Repository(lm_pk610).query(start, last.saturday(), *report_sections(*cuts)))


async def weekly_formula(start: date, end: date, *cuts: Cut) -> Iterator[Sales]:
    first = Week.withdate(start) + 1
    last = Week.withdate(end) + 1
    start = first.monday()

    if last.day(lm_pk620.weekday) < lm_pk620.latest:
        last -= 1

    return map(parse_record, await Repository(lm_pk620).query(start, last.saturday(), *report_sections(*cuts)))
