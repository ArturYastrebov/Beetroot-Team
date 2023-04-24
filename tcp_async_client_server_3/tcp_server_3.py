import asyncio
import random
from dataclasses import dataclass

@dataclass
class Connect:
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter

class Server():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect: Connect = None
        self.queue = asyncio.Queue()
        self.sessions = {}

    async def handler_request(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        addr = writer.get_extra_info("peername")
        ip = addr[1]
        self.sessions[ip] = writer
        self.connect = Connect(reader, writer)
        print(f'Client with ip:{ip} connection')
        while True:
            bite_request = await reader.read(1024)
            request = bite_request.decode('utf-8')
            print(f'Receive message from {ip}: {request}')
            await self.queue.put((request, writer))

    async def task(self, request):
            rnd = random.randint(1, 5)
            await asyncio.sleep(rnd)
            for session in self.sessions.values():
                msg = f'message {request} has delay {rnd}'
                session.write(msg.encode('utf-8'))
                await session.drain()
                # await self.close_connection()

    async def process_requests(self):
        while 1:
            request, writer = await self.queue.get()
            await self.task(request)


    async def close_connection(self):
        print('Close connection')
        self.connect.writer.close()
        await self.connect.writer.wait_closed()

    async def start_server(self):
        print(f"Start server on host {self.host}")
        server = await asyncio.start_server(self.handler_request, self.host, self.port)
        await asyncio.create_task(self.process_requests())
        async with server:
            await server.serve_forever()

async def main():
    server = Server('Localhost', 8383)
    await server.start_server()


if __name__ == "__main__":
    asyncio.run(main())
