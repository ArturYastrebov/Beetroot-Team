import asyncio
import random
from dataclasses import dataclass

HOST = "localhost"
PORT = 7777

sessions = {}

@dataclass
class Request:
    identification: str
    device:  dict
    connection: str
    status: str


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    port = addr[1]
    sessions[port] = writer
    print(f"New connection from {addr!r}")
    while True:
        data = await reader.read(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received {message!r}")
        rnd = random.randint(1, 7)
        print(f'message {message} has delay {rnd}')
        await asyncio.sleep(rnd)
        for session in sessions.values():
            session_message = f"Message from {port}: {message}".encode()
            session.write(session_message)
            await session.drain()
    await writer.wait_closed()
    print(f"{port} was deleted")


async def main():
    server = await asyncio.start_server(
        handle_client, HOST, PORT)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
