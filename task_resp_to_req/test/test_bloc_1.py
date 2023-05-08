import pytest
import pytest_asyncio
import asyncio

Response3 = '{"result": "success", "data": {"users": [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]}}'
Response4 = '{"result": "success2", "data": {"users": [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]}}'
Request3 = '{"request_id": "success", "data": "1&&id&&1&&name&&Alice&&age&&30%%2&&id&&2&&name&&Bob&&age&&25"}'
Request4 = '{"request_id": "success2", "data": "1&&id&&1&&name&&Alice&&age&&30%%2&&id&&2&&name&&Bob&&age&&25"}'


@pytest.mark.asyncio
@pytest.mark.parametrize('req, resp', [(Response3, Request3), (Response4, Request4)])
async def test_sent_req_param(client, req, resp):
    await client.write_message(req)
    expected_result = await client.read_message()
    assert expected_result.decode('utf-8') == resp


@pytest.mark.asyncio
async def test_sent_req_param_fixture(client, parametrize_req):
    REQ, RESP = parametrize_req
    await client.write_message(REQ)
    expected_result = await client.read_message()
    assert expected_result.decode('utf-8') == RESP

