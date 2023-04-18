import pytest

from client import TCPAsyncClient

class TestServer:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("message, expected", (
                             ('{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}',
                              '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "25", "reaction": "Nothing"}, "Car2": {"speed": "35", "reaction": "Nothing"}}}'),
                             ('{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&45%%Car2&&speed&&60%%"}',
                              '{"request_id": "01", "data": {"Car1": {"name": "some_name", "speed": "45", "reaction": "Nothing"}, "Car2": {"speed": "60", "reaction": "Penalty"}}}')
                             ))
    async def test_sent_valid_data(self, client: TCPAsyncClient, message, expected):
        await client.send_message(message)
        response = await client.listen_answer()
        assert response == expected


    @pytest.mark.asyncio
    async def test_sent_invalid_json_data(self, client: TCPAsyncClient, create_invalid_json_data):
        message = create_invalid_json_data
        await client.send_message(message)
        response = await client.listen_answer()
        assert response == "Data Error. Not correct json file."

    @pytest.mark.asyncio
    async def test_sent_not_json_data(self, client: TCPAsyncClient, create_not_json_data):
        message = create_not_json_data
        await client.send_message(message)
        response = await client.listen_answer()
        assert response == "Data Error. Is not json format."

def test_simple():
    assert 1 == 1
