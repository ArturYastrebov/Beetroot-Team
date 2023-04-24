import asyncio
from dataclasses import dataclass

from aioconsole import ainput


@dataclass
class Connect:
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect: Connect = None

    async def sent_message(self):
        while True:
            msg = await ainput("Enter message: ")
            print(f'sent message to server {msg}')
            response = msg.encode('utf-8')
            self.connect.writer.write(response)
            await self.connect.writer.drain()

    async def get_message(self):
        while 1:
            bite_request = await self.connect.reader.read(1024)
            if not bite_request:
                break
            request = bite_request.decode('utf-8')
            print(f'get message from server: {request}')

    async def close_connection(self):
        print('close connection')
        self.connect.writer.close()
        await self.connect.writer.wait_closed()

    async def connect_to_server(self):
        print('connect to server')
        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.connect = Connect(reader, writer)


async def main():
    client = Client('localhost', 8383)
    await client.connect_to_server()
    await asyncio.gather(client.sent_message(), client.get_message())


if "__main__" == __name__:
    asyncio.run(main())
