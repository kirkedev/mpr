from aiohttp.test_utils import TestServer
from pytest import fixture

from .server import server


@fixture
async def mpr_server() -> TestServer:
    return TestServer(server, port=8080)
