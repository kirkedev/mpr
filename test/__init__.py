from typing import Iterator
from typing import TextIO
from xml.etree import ElementTree

from aiohttp.web_fileresponse import FileResponse
from aiohttp.web_request import Request
from aiohttp.web_routedef import RouteTableDef

from mpr.api import Attributes
from mpr.api import parse_elements

routes = RouteTableDef()


@routes.get("/ws/report/v1/hogs/lm_pk602")
def lm_pk602(_: Request):
    return FileResponse('test/resources/server/LM_PK602_06-03-2019_06-09-2019.xml')


def parse_report(report: TextIO) -> Iterator[Attributes]:
    elements = ElementTree.iterparse(report, events=['start', 'end'])
    return parse_elements(elements)


def load_resource(name: str) -> Iterator[Attributes]:
    with open(f"test/resources/{name}") as report:
        for element in parse_report(report):
            yield element
