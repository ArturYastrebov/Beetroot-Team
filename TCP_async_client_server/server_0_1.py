import asyncio
from dataclasses import dataclass


@dataclass
class Connect:
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect = None

    async def hendler_message(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.connect = Connect(reader, writer)
        reqeust = await self.lisner()
        await self.answer(reqeust)
        print('server wait for message')


    async def lisner(self):
        while True:
            data = await self.connect.reader.read(1024)
            if not data:
                break
            msg = data.decode("utf-8")
            print(f'get answer from {self.connect.writer.get_extra_info("peername")} {msg}')
            return msg


    async def answer(self, msg):
        request = msg.encode('utf-8')
        self.connect.writer.write(request)
        print(f'sent message {msg}')
        await self.connect.writer.drain()


    async def start(self):
        server = await asyncio.start_server(self.hendler_message, self.host, self.port)
        print(f'Server running on port {self.port}')
        async with server:
            await server.serve_forever()


async def main():
    server = Server('localhost', 8000)
    await server.start()

if __name__ == "__main__":
    asyncio.run(main())





