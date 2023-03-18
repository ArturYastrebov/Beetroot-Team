import asyncio

from tcp_test.config import HOST, PORT


async def tcp_client(message):
    reader, writer = await asyncio.open_connection(host=HOST, port=PORT)
    print(f'send message {message}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(1000)
    response = data.decode()
    print(f'receive message {response}')

if __name__ == "__main__":
    REQ = '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}'
    asyncio.run(tcp_client(REQ))
