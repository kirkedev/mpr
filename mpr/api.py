import json
from typing import TypeVar
from typing import Optional
from typing import Tuple
from typing import Dict
from typing import Iterator
from os import environ
from datetime import date
from itertools import zip_longest
from io import BytesIO
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

import aiohttp
from aiohttp import TCPConnector

from numpy import uint32
from numpy import float32
from numpy import nan

from .report import Report
from .report import Section

T = TypeVar('T')
Attributes = Dict[str, str]
ParsedElement = Tuple[str, Element]

date_format = "%m-%d-%Y"


def report_url(report: Report) -> str:
    host = environ.get('HOST', 'http://localhost:8080')
    return f'{host}/ws/report/v1/hogs/{report}'


def date_filter(start: date, end: date) -> str:
    return json.dumps({
        'fieldName': 'Report date',
        'operatorType': 'BETWEEN',
        'values': [
            start.strftime(date_format),
            end.strftime(date_format)
        ]
    })


def request_url(report: Report, start: date, end: date) -> str:
    return f'{report_url(report)}?filter={{"filters":[{date_filter(start, end)}]}}'


def strip_commas(value: str) -> str:
    return value.replace(',', '')


def get_optional(attr: Attributes, key: str) -> Optional[str]:
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


def filter_section(records: Iterator[Attributes], section: Section) -> Iterator[Attributes]:
    return filter(lambda it: it['label'] == section, records)


def filter_sections(records: Iterator[Attributes], *args: Section) -> Iterator[Iterator[Attributes]]:
    attrs = filter(lambda it: it['label'] in args, records)
    return chunk(attrs, len(args))


async def fetch(report: Report, start: date, end=date.today()) -> Iterator[Attributes]:
    url = request_url(report=report.name, start=start, end=end)

    async with aiohttp.ClientSession(connector=TCPConnector(limit=4)) as session:
        async with session.get(url) as response:
            data = BytesIO(await response.read())
            elements = ElementTree.iterparse(data, events=['start', 'end'])
            return parse_elements(elements)


def parse_elements(elements: Iterator[ParsedElement], min_depth=1, max_depth=4) -> Iterator[Attributes]:
    """
    Parses a USDA report by saving metadata from parent elements to a dictionary while traversing down the tree.
    When at the maximum depth, yield all collected metadata with each child element's attributes.

    Typical layout of a USDA report:
     <results exportTime>
        <report label slug>
            <record report_date reported_for_date>
                <report label>
                    <record ...attributes/>

    Usually all we care about is the report date (depth=2); the report section label (depth=3);
    and the record data attributes (depth=4).
    """
    depth = 0
    metadata: Attributes = dict()

    for event, element in elements:
        if event == 'start':
            if min_depth <= depth < max_depth:
                # Parsing a parent element: merge its properties into the metadata
                metadata.update(element.items())

            elif depth == max_depth:
                # Parsing a child element: generate a dict combining metadata and child attributes
                yield dict(metadata.items() | element.items())

            depth += 1

        if event == 'end':
            depth -= 1

            if depth == min_depth:
                # clear the metadata and element tree after each report section
                element.clear()
                metadata.clear()
