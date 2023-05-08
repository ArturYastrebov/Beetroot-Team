import asyncio
from dataclasses import dataclass

@dataclass
class Connect:
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect = Connect

    async def connect_to_server(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        print(f'Connect to server {self.host}')
        self.connect = Connect(reader, writer)

    async def sent_message(self, msg):
        data = msg.encode('utf-8')
        print(f'sent message {msg}')
        self.connect.writer.write(data)
        await self.connect.writer.drain()

    async def get_answer(self):
        data = await self.connect.reader.read(1024)
        msg = data.decode('utf-8')
        print(f'Get message: {msg}')
        return msg

    async def close_connect(self):
        self.connect.writer.close()
        print('close connect')
        await self.connect.writer.wait_closed()


async def main():
    client = Client('localhost', 8282)
    await client.connect_to_server()
    await client.sent_message('hello server')
    await client.get_answer()
    await client.close_connect()

if __name__ == "__main__":
    asyncio.run(main())
