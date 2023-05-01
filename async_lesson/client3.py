import asyncio
from datetime import datetime

from aioconsole import ainput

HOST = "localhost"
PORT = 8383


# async def write_message(writer: asyncio.StreamWriter, data: bytes):
#     writer.write(data)
#     await writer.drain()


async def listen(reader: asyncio.StreamReader):
    print("Listening...")
    while True:
        print("Waiting for message...")
        data = await reader.read(1024)
        message = data.decode()
        if not message:
            raise Exception("Connection closed")
        print(f"Received {message!r}")


async def enter_messages(writer: asyncio.StreamWriter):
    while True:
        message = await ainput("Enter message: ")
        # await write_message(writer, message.encode("utf-8"))
        writer.write(message.encode())
        await writer.drain()
        print(f"Sent {message!r}")




async def start_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    await asyncio.gather(listen(reader), enter_messages(writer))


asyncio.run(start_client())
