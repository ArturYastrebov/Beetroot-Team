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
        self.connect: Connect = None

    async def sent_message(self, msg):
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
    client = Client('localhost', 8080)
    await client.connect_to_server()
    await client.sent_message('Hello1')
    await asyncio.sleep(1)
    await client.sent_message('GoodJob')
    while 1:
        await client.get_message()




if "__main__" == __name__:
    asyncio.run(main())
