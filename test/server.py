import json

from aiohttp.test_utils import TestServer

from aiohttp.web import Request
from aiohttp.web import FileResponse
from aiohttp.web import get
from aiohttp.web_app import Application

from mpr import lm_hg200
from mpr import lm_hg201
from mpr import lm_pk602
from mpr.data.report import Report


def route(report: Report):
    async def handler(request: Request) -> FileResponse:
        filters = json.loads(request.query.get('filter'))
        start, end = filters.get('filters')[0].get('values')
        return FileResponse(f"test/resources/server/{report}_{start}_{end}.xml")

    return get(f"/ws/report/v1/hogs/{report}", handler)


routes = [
    route(lm_hg200),
    route(lm_hg201),
    route(lm_pk602)
]


def server() -> TestServer:
    app = Application()
    app.add_routes(routes)
    return TestServer(app, port=8080)
