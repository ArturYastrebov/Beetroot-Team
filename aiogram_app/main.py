import logging
import aiohttp
from aiogram import Bot, Dispatcher, executor, types

from aiogram_app.config import TOKKEN
from aiogram_app.keybords import subscribers_keyboard
from sql_app.config import HOST

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["info"], commands_prefix="|")
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f"ID: {message.from_user.id}")
    await bot.send_message(message.from_user.id, f"FIRST NAME: {message.from_user.first_name}")
    await bot.send_message(message.from_user.id, f"LAST NAME: {message.from_user.last_name}")
    await bot.send_message(message.from_user.id, f"FULL NAME: {message.from_user.full_name}")
    await bot.send_message(message.from_user.id, f"USER NAME: {message.from_user.username}")
    await bot.send_message(message.from_user.id, f"VALUES: {message.from_user.values}")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Hello: {message.from_user.id}", reply_markup=subscribers_keyboard())


@dp.callback_query_handler(text="cd_btn_subscr")
async def command_btn_subscr(query: types.CallbackQuery):
    user_id = query.message.chat.id
    user_name = query.message.chat.username if query.message.chat.username is not None else query.message.chat.full_name
    await query.message.delete()

    url = HOST + "users/"
    payload = {"chat_id": user_id, "nickname": user_name}
    print("payload =", payload)
    headers = {"content-type": "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, ssl=False, headers=headers) as resp:
            print(resp.status)
            print(await resp.text())
            if resp.status == 201:
                await bot.send_message(user_id, "Congratulations, you have subscribed to the newsletter")
            elif resp.status == 400:
                await bot.send_message(user_id, "You already have a subscription")


@dp.callback_query_handler(text="cd_btn_unsubscr")
async def command_btn_unsubscr(query: types.CallbackQuery):
    user_id = query.message.chat.id
    await query.message.delete()
    url = HOST + "users/"
    payload = {"chat_id": user_id}
    print("payload =", payload)
    headers = {"content-type": "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.delete(url, json=payload, ssl=False, headers=headers) as resp:
            print(resp.status)
            print(await resp.text())
            if resp.status == 200:
                await bot.send_message(user_id, "You have unsubscribed from the newsletter")
            elif resp.status == 400:
                await bot.send_message(user_id, "You haven't a subscription")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
