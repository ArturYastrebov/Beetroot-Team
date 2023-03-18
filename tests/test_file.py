import pytest

from tcp_test.tests.conftest import check_reaction

@pytest.mark.asyncio
async def test_json_data(client, test_parametrized_data):
    reader, writer = await client
    message = test_parametrized_data
    writer.write(message.encode())
    await writer.drain()
    response = await reader.read(1000)
    assert check_reaction(response.decode())

@pytest.mark.asyncio
async def test_error_json_data(client):
    reader, writer = await client
    message = '{"dsad"}'
    writer.write(message.encode())
    await writer.drain()
    response = await reader.read(1000)
    assert response.decode() == 'Data Error'


