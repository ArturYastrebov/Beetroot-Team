import pytest
import pytest_asyncio



@pytest.mark.asyncio
async def test_sent_correct_msg(client):
    REQ = '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}'
    await client.sent_message(REQ)
    response = await client.read_message_one_times()
    expected_result = '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "25", "reaction": "Nothing"}, "Car2": {"speed": "35", "reaction": "Nothing"}}}'
    assert response == expected_result

REQ1 = '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&38%%Car2&&speed&&56%%"}'
RESP1 = '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "38", "reaction": "Nothing"}, "Car2": {"speed": "56", "reaction": "Penalty"}}}'
REQ2 = '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&60%%Car2&&speed&&30%%"}'
RESP2 = '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "60", "reaction": "Penalty"}, "Car2": {"speed": "30", "reaction": "Nothing"}}}'

@pytest.mark.asyncio
@pytest.mark.parametrize('req, expected_result',[
    ('{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&38%%Car2&&speed&&56%%"}',
     '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "38", "reaction": "Nothing"}, "Car2": {"speed": "56", "reaction": "Penalty"}}}'),
    ('{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&60%%Car2&&speed&&30%%"}',
     '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "60", "reaction": "Penalty"}, "Car2": {"speed": "30", "reaction": "Nothing"}}}')])
async def test_parametrize_sent_correct_msg(client, req, expected_result):
    await client.sent_message(req)
    response = await client.read_message_one_times()
    assert response == expected_result

@pytest.mark.asyncio
async def test_parametrize_fixture_sent_correct_msg(client, parametrize_fixture):
    req, expected_result = parametrize_fixture
    await client.sent_message(req)
    response = await client.read_message_one_times()
    assert response == expected_result




