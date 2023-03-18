import pytest

from tests.conftest import check_reaction

@pytest.mark.asyncio
async def test_json_data(client, params_data):
    reader, writer = await client
    message, expected = params_data
    writer.write(message.encode())
    await writer.drain()
    response = await reader.read(1000)
    assert response.decode() == expected

@pytest.mark.asyncio
@pytest.mark.parametrize('not_json_data', ['{"wrong_data_type1"}', '{"wrong_data_type2"}'])
async def test_error_json_data(client, not_json_data):
    reader, writer = await client
    message = not_json_data
    writer.write(message.encode())
    await writer.drain()
    response = await reader.read(1000)
    assert response.decode() == 'Data Error'


