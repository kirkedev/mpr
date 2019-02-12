from typing import Iterator
from xml.etree import ElementTree
from io import StringIO

from mpr.data.api import ParsedElement
from mpr.data.api import Attributes
from mpr.data.api import parse_elements

def load_report(report: str) -> Iterator[ParsedElement]:
    return ElementTree.iterparse(StringIO(report), events=['start', 'end'])

def parse_report(report: str) -> Iterator[Attributes]:
    return parse_elements(load_report(report))
