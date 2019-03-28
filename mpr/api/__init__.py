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

from numpy import uint32
from numpy import float32
from numpy import nan

from ..reports import Report

T = TypeVar('T')
Attributes = Dict[str, str]
ParsedElement = Tuple[str, Element]

date_format = "%m-%d-%Y"

base_url = 'https://mpr.datamart.ams.usda.gov/ws/report/v1/hogs'
report_url = lambda report: f'{base_url}/{report}'
date_filter = lambda start, end: f'{{"fieldName":"Report date","operatorType":"BETWEEN","values":["{start}","{end}"]}}'
request_url = lambda report, start, end: f'{report_url(report)}?filter={{"filters":[{date_filter(start, end)}]}}'


def strip_commas(value: str) -> str:
    return value.replace(',', '')


def get_optional(attr: Attributes, key: str) -> Optional[T]:
    return attr[key] if key in attr and attr[key] != 'null' else None


def opt_float(attr: Attributes, key: str) -> float32:
    value = get_optional(attr, key)
    return float32(strip_commas(value)) if value else nan


def opt_int(attr: Attributes, key: str) -> uint32:
    value = get_optional(attr, key)
    return uint32(strip_commas(value)) if value else 0


def chunk(iterator: Iterator[T], n: int) -> Iterator[Iterator[T]]:
    args = [iterator] * n
    return zip_longest(*args, fillvalue=None)


def filter_section(records: Iterator[Attributes], section: str) -> Iterator[Attributes]:
    return filter(lambda it: it['label'] == section, records)


def filter_sections(records: Iterator[Attributes], *args: str) -> Iterator[Iterator[Attributes]]:
    attrs = filter(lambda it: it['label'] in args, records)
    return chunk(attrs, len(args))


async def fetch(report: Report, start_date: date, end_date=date.today()) -> Iterator[Attributes]:
    url = request_url(
        report=report.value,
        start=start_date.strftime(date_format),
        end=end_date.strftime(date_format))

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = BytesIO(await response.read())
            elements = ElementTree.iterparse(data, events=['start', 'end'])
            return parse_elements(elements)


def parse_elements(elements: Iterator[ParsedElement], max_depth=4) -> Iterator[Attributes]:
    """
    Parses a USDA report by saving metadata from parent elements to a dictionary while traversing down the tree.
    When at the maximum depth, yield all collected metadata with each child element's attributes.

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
    metadata: Attributes = dict()

    for event, element in elements:
        if event == 'start':
            if 1 <= depth < max_depth:
                # Parsing a parent element: merge its properties into the metadata
                metadata.update(element.items())

            elif depth == max_depth:
                # Parsing a child element: combine its properties with the metadata and yield
                yield dict(metadata.items() | element.items())

            depth += 1

        if event == 'end':
            depth -= 1

            if depth == 2:
                # Finished parsing one day's data: clear the metadata and element tree
                element.clear()
                metadata.clear()
