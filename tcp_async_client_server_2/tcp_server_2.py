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
    async def handler_request(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.connect = Connect(reader, writer)
        addr = writer.get_extra_info('peername')[0]
        print(f'Client with ip:{addr} connection')
        bite_request = await reader.read(1024)
        request = bite_request.decode('utf-8')
        print(f'Receive message from {addr}: {request}')
        await asyncio.sleep(random.randint(1, 5))
        writer.write(request.encode('utf-8')*2)
        await writer.drain()
        # await self.close_connection()

    async def close_connection(self):
        print('Close connection')
        self.connect.writer.close()
        await self.connect.writer.wait_closed()

    async def start_server(self):
        print(f"Start server on host {self.host}")
        server = await asyncio.start_server(self.handler_request, self.host, self.port)
        async with server:
            await server.serve_forever()

async def main():
    server = Server('Localhost', 8080)
    await server.start_server()

if __name__ == "__main__":
    asyncio.run(main())
