import json

from aiohttp.test_utils import TestServer
from aiohttp.web import Application
from aiohttp.web import FileResponse
from aiohttp.web import Request
from aiohttp.web import get

from mpr.cutout.report import lm_pk602
from mpr.data.report import Report
from mpr.purchases.report import lm_hg200
from mpr.sales.report import lm_pk610
from mpr.sales.report import lm_pk620
from mpr.slaughter.report import lm_hg201


def route(report: Report):
    async def handler(request: Request) -> FileResponse:
        filters = json.loads(request.query.get('filter'))
        start, end = filters.get('filters')[0].get('values')
        return FileResponse(f"test/resources/server/{report}_{start}_{end}.xml")

    return get(f"/ws/report/v1/hogs/{report}", handler)


routes = [
    route(lm_hg200),
    route(lm_hg201),
    route(lm_pk602),
    route(lm_pk610),
    route(lm_pk620)
]


def server() -> TestServer:
    app = Application()
    app.add_routes(routes)
    return TestServer(app, port=8080)
