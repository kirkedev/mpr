import json

from aiohttp.web import Application
from aiohttp.web import Request
from aiohttp.web import FileResponse
from aiohttp.web import get

from mpr.report import CutoutReport
from mpr.report import Report
from mpr.report import SlaughterReport


def route(report: Report):
    async def handler(request: Request) -> FileResponse:
        filters = json.loads(request.query.get('filter')).get('filters')
        start, end = filters[0].get('values')
        return FileResponse(f"test/resources/server/{report.name}_{start}_{end}.xml")

    return get(f"/ws/report/v1/hogs/{report.name}", handler)


server = Application()

server.add_routes([
    route(SlaughterReport.LM_HG201),
    route(CutoutReport.LM_PK602)
])
