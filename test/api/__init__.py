from typing import Iterator, TextIO
from xml.etree import ElementTree
from io import StringIO

from mpr.data.api import ParsedElement
from mpr.data.api import Attributes
from mpr.data.api import parse_elements

def load_report(report: str) -> Iterator[ParsedElement]:
    return parse_report(StringIO(report))

def parse_report(report: TextIO) -> Iterator[Attributes]:
    elements = ElementTree.iterparse(report, events=['start', 'end'])
    return parse_elements(elements)

def load_resource(path: str) -> Iterator[ParsedElement]:
    with open(path) as report:
        for element in parse_report(report):
            yield element
