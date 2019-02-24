from typing import TypeVar
from typing import Optional
from typing import Tuple
from typing import Dict
from typing import Iterator
from datetime import date
from itertools import zip_longest
from io import BytesIO
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

import aiohttp

import numpy as np
from numpy import uint32
from numpy import float32
from numpy import nan

from mpr.data import Report

T = TypeVar('T')
Attributes = Dict[str, str]
ParsedElement = Tuple[str, Element]
DateInterval = Tuple[date, date]

date_format = "%m-%d-%Y"

base_url = 'https://mpr.datamart.ams.usda.gov/ws/report/v1/hogs/{report}?\
filter={{"filters":[{{"fieldName":"Report date","operatorType":"BETWEEN","values":["{start_date}", "{end_date}"]}}]}}'


def get_optional(attr: Attributes, key: str) -> Optional[T]:
    return attr[key] if key in attr and attr[key] != 'null' else None


def opt_float(attr: Attributes, key: str) -> float32:
    value = get_optional(attr, key)
    return float32(value.replace(',', '')) if value else nan


def opt_int(attr: Attributes, key: str) -> uint32:
    value = get_optional(attr, key)
    return uint32(value.replace(',', '')) if value else 0


def date_interval(days: int) -> DateInterval:
    today = date.today()
    start = np.busday_offset(today, -days, 'backward').astype('O')
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
    """
    Parses a USDA report by saving metadata from parent elements to a dictionary while traversing down the tree.
    When at the maximum depth (4), yield all collected metadata with each child element's attributes.

    Typical layout of a USDA report:
     <results exportTime>
        <report label slug>
            <record report_date reported_for_date>
                <report label>
                    <record ...attributes/>

    Usually all we care about is the report date (depth=2); the report label (depth=3), for finding sections;
    and the record attributes (depth=4), which contains the data.
    """
    depth = 0
    metadata: Dict[str, str] = dict()

    for event, element in elements:
        if event == 'start':
            if 1 <= depth < 4:
                # Parsing a parent element: merge its properties into the metadata
                metadata.update(element.items())
            elif depth == 4:
                # Parsing a child element: combine its properties with the metadata and yield
                yield dict(metadata.items() | element.items())

            depth += 1

        if event == 'end':
            depth -= 1

            if depth == 2:
                # Finished parsing one day's data: clear the metadata and element tree
                element.clear()
                metadata.clear()
