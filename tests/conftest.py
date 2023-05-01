import asyncio
import pytest
import pytest_asyncio

from TCP_async_client_server.client_0_1 import Client
from TCP_async_client_server.server_0_1 import Server

@pytest_asyncio.fixture()
async def client():
    client = Client('localhost', 8000)
    await client.connect_to_server()
    yield client
    await client.close_connect()

@pytest_asyncio.fixture(params=(('111','111'), ('222','222')))
async def param_fixture(request):
    return request.param
