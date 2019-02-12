from enum import Enum
from typing import Optional
from typing import Tuple
from typing import Dict
from typing import Iterator
from typing import TypeVar
from datetime import date
from itertools import zip_longest
from io import BytesIO
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

import aiohttp
import numpy as np

T = TypeVar('T')
Attributes = Dict[str, str]
ParsedElement = Tuple[str, Element]

date_format = "%m-%d-%Y"

base_url = 'https://mpr.datamart.ams.usda.gov/ws/report/v1/hogs/{report}?\
filter={{"filters":[{{"fieldName":"Report date","operatorType":"BETWEEN","values":["{start_date}", "{end_date}"]}}]}}'


class Report(Enum):
    PURCHASED_SWINE = 'LM_HG200'
    SLAUGHTERED_SWINE = 'LM_HG201'
    DIRECT_HOG_MORNING = 'LM_HG202'
    DIRECT_HOG_AFTERNOON = 'LM_HG203'
    CUTOUT_MORNING = 'LM_PK602'
    CUTOUT_AFTERNOON = 'LM_PK603'


def get_optional(attr: Attributes, key: str) -> Optional[str]:
    return attr[key] if key in attr and attr[key] != 'null' else None


def opt_float(attr: Attributes, key: str) -> Optional[float]:
    value = get_optional(attr, key)
    return float(value.replace(',', '')) if value else None


def opt_int(attr: Attributes, key: str) -> Optional[int]:
    value = get_optional(attr, key)
    return int(value.replace(',', '')) if value else None


def date_interval(days: int) -> Tuple[date, date]:
    today = date.today()
    start = np.busday_offset(today, -days).astype('O')
    return start, today


def chunk(iterator: Iterator[T], n: int) -> Iterator[Iterator[T]]:
    args = [iterator] * n
    return zip_longest(*args, fillvalue=None)


def filter_section(records: Iterator[Attributes], section: str) -> Iterator[Attributes]:
    return filter(lambda it: it['label'] == section, records)


def filter_sections(records: Iterator[Attributes], *args: str) -> Iterator[Iterator[Attributes]]:
    attrs = filter(lambda it: it['label'] in args, records)
    return chunk(attrs, len(args))


async def fetch(report: Report, start_date: date, end_date=date.today()) -> Iterator[Attributes]:
    url = base_url.format(
        report=report.value,
        start_date=start_date.strftime(date_format),
        end_date=end_date.strftime(date_format))

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = BytesIO(await response.read())
            elements = ElementTree.iterparse(data, events=['start', 'end'])
            return parse_elements(elements)


def parse_elements(elements: Iterator[ParsedElement]) -> Iterator[Attributes]:
    depth = 0
    metadata: Dict[str, str] = dict()

    for event, element in elements:
        if event == 'start':
            # Currently parsing a parent element, merge its properties into the metadata
            if depth < 4:
                metadata.update(element.items())

            # Found the child element, combine its properties with the metadata and yield
            else:
                yield dict(metadata.items() | element.items())

            depth += 1

        if event == 'end':
            depth -= 1

            # After parsing a full day's report, clear the metadata and parsed tree
            if depth == 2:
                element.clear()
                metadata.clear()
