from typing import Iterator
from typing import TextIO
from io import StringIO
from xml.etree import ElementTree

from mpr.data.api import Attributes
from mpr.data.api import parse_elements


def parse_report(report: TextIO) -> Iterator[Attributes]:
    elements = ElementTree.iterparse(report, events=['start', 'end'])
    return parse_elements(elements)


def load_report(report: str) -> Iterator[Attributes]:
    return parse_report(StringIO(report))


def load_resource(name: str) -> Iterator[Attributes]:
    with open(f"test/resources/{name}") as report:
        for element in parse_report(report):
            yield element
