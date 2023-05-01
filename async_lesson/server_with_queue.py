import asyncio
import random

# создаем очередь для запросов
queue = asyncio.Queue()

async def handle_request(reader, writer):
    global queue
    request = await reader.read(1024)  # читаем входящий пакет
    print(request.decode())

    # добавляем запрос в очередь
    await queue.put((request, writer))

async def process_requests(queue):
    while True:
        # получаем следующий запрос из очереди
        request, writer = await queue.get()

        # ждем случайный таймаут
        await asyncio.sleep(random.uniform(1, 5))

        response = b'RESP'  # формируем ответ
        writer.write(response)  # отправляем ответ клиенту
        await writer.drain()
        #
        # writer.close()
        # await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_request, 'localhost', 8888)
    async with server:
        global queue

        # запускаем цикл обработки запросов
        asyncio.create_task(process_requests(queue))

        # запускаем сервер
        await server.serve_forever()

asyncio.run(main())