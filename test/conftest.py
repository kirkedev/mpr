from aiohttp.test_utils import TestServer
from aiohttp.web import Application
from pytest import fixture

from .routes import routes


@fixture
def mpr_server() -> TestServer:
    server = Application()
    server.add_routes(routes)
    return TestServer(server, port=8080)
