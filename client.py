import asyncio
import dataclasses

from config import HOST, PORT


@dataclasses.dataclass
class Connect:
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter


class TCPAsyncClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect = Connect

    async def open_connection(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.connect = Connect(reader, writer)

    async def send_message(self, message):
        self.connect.writer.write(message.encode())
        await self.connect.writer.drain()

    async def listen_answer(self):
        while True:
            response = await self.connect.reader.read(1024)
            return response.decode()

    def disconnect(self):
        if self.connect.writer:
            self.connect.writer.close()

    async def wait_closed(self):
        if self.connect.writer:
            await self.connect.writer.wait_closed()


client = TCPAsyncClient(HOST, PORT)


async def main():
    await client.open_connection()
    REQ = '{"request_id": "01", "data": "Car1&&name&&some_name&&speed&&25%%Car2&&speed&&35%%"}'
    await client.send_message(REQ)
    print(await client.listen_answer())
    client.disconnect()
    await client.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
