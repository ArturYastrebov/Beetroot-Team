import asyncio
from datetime import datetime

from aioconsole import ainput

HOST = "localhost"
PORT = 9999


async def write_message(writer: asyncio.StreamWriter, data: bytes):
    writer.write(data)
    await writer.drain()


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
    for i in range(10):
        message = await ainput("Enter message: ")
        await write_message(writer, message.encode("utf-8"))
        print(f"Sent {message!r}")

async def sent_list_messages(writer: asyncio.StreamWriter, msg):
        await asyncio.sleep(1)
        print(f"Sent {msg!r}")
        await write_message(writer, msg.encode("utf-8"))



async def start_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    list_msg = ['Hello', '124', '111222']
    await asyncio.gather(listen(reader), sent_list_messages(writer, 'list_msg'), sent_list_messages(writer, '123'), sent_list_messages(writer, 'listdasdas_msg'))


asyncio.run(start_client())
