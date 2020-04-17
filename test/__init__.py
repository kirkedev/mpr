from typing import Iterator
from typing import TextIO
from xml.etree import ElementTree

from mpr.data.client import Record
from mpr.data.client import parse_elements


def parse_report(report: TextIO) -> Iterator[Record]:
    elements = ElementTree.iterparse(report, events=['start', 'end'])
    return parse_elements(elements)


def load_resource(name: str) -> Iterator[Record]:
    with open(f"test/resources/{name}") as report:
        for element in parse_report(report):
            yield element
