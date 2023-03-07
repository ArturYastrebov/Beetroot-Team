import asyncio
from aioconsole import ainput

HOST = "localhost"
PORT = 8080


async def listen(reader: asyncio.StreamReader):
    print("Listening...")
    while True:
        print("Waiting for message...")
        data = await reader.read(1024)
        message = data.decode()
        if not message:
            raise Exception("Connection closed")
        print(f"Received {message}")


async def enter_messages(writer: asyncio.StreamWriter):
    while True:
        message = await ainput("Enter message: ")
        writer.write(message.encode())
        await writer.drain()
        print(f"Sent {message!r}")


async def start_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    await asyncio.gather(listen(reader), enter_messages(writer))


asyncio.run(start_client())
