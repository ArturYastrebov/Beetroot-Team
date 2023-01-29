from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiofiles import os

from config import TOKEN
from formatter import Formatter
from mono_api import my_mono, my_privat, my_wallet

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


class ClientStatesGroup(StatesGroup):
    amount_of_money = State()
    amount_of_mounths = State()


class BankGroup(StatesGroup):
    privat = State()
    mono = State()


def get_kb_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text="/cancel"))
    return kb


def get_kb_back_privat() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text="<== PrivatBank"))
    return kb


def get_kb_back_mono() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text="<== MonoBank"))
    return kb


def get_kb_bank() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="PrivatBank")
    button2 = KeyboardButton(text="MonoBank")
    kb.add(button1, button2)
    return kb


def get_kb_PrivatBank() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="Зробити $ вклад")
    button2 = KeyboardButton(text="Курс $")
    button3 = KeyboardButton(text="Деталі $ вкладу")
    button4 = KeyboardButton(text="<== Головне меню")
    kb.add(button1, button2, button3).add(button4)
    return kb


def get_kb_MonoBank() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button2 = KeyboardButton(text="Курс $")
    button4 = KeyboardButton(text="<== Головне меню")
    kb.add(button2).add(button4)
    return kb


@dp.message_handler(commands="start")
@dp.message_handler(text="<== Головне меню", state="*")
async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://sfvbareferral.com/wp-content/uploads/2018/11/Can-I-Get-My-Security-Deposit-Back-If-I-Never"
              "-Signed-a-Lease.png.webp",
    )
    await message.answer(
        "Вітаємо в deposit_bot. \nВи можете переглянути актуальну інформацію про курс долара та зробити "
        "розрахунок коштів на певний період часу\n"
    )
    print(f"Client {message.from_user.id} on start menu")
    await message.answer("Виберіть банк:", reply_markup=get_kb_bank())


@dp.message_handler(text=["PrivatBank", "<== PrivatBank"], state="*")
async def PrivatBank(message: types.Message):
    print(f"Client {message.from_user.id} on privat menu")
    await BankGroup.privat.set()
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://upload.wikimedia.org/wikipedia/commons/7/73/%D0%9F%D1%80%D0%B8%D0%B2%D0%B0%D1%82%D0%91%D0%B0"
              "%D0%BD%D0%BA.png",
    )
    await message.answer("PrivatBank меню:", reply_markup=get_kb_PrivatBank())


@dp.message_handler(text="Курс $", state=BankGroup.privat)
async def PrivatBank(message: types.Message):
    print(f"Client {message.from_user.id} on Курс $ privat")
    text = my_privat.exchange_rate()
    await message.answer(text, reply_markup=get_kb_back_privat())


@dp.message_handler(text="Деталі $ вкладу", state=BankGroup.privat)
async def PrivatBank(message: types.Message):
    print(f"Client {message.from_user.id} on Деталі $ вкладу privat")
    text = my_privat.details()
    await message.answer(text, reply_markup=get_kb_back_privat())


@dp.message_handler(text="Зробити $ вклад", state=BankGroup.privat)
async def PrivatBank(message: types.Message, state: FSMContext):
    print(f"Client {message.from_user.id} on Зробити $ вклад privat")
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://sfvbareferral.com/wp-content/uploads/2018/11/Can-I-Get-My-Security-Deposit-Back-If-I-Never" \
             "-Signed-a-Lease.png.webp",
    )
    await ClientStatesGroup.amount_of_money.set()
    await message.answer(
        "Обмеження суми на відкриття депозиту 100 000грн в місяць.\n"
        "Рекомендована сума вкладу має бути кратна 100 000 грн."
    )
    await message.answer("Введіть суму вкладу в гривнях:")


@dp.message_handler(
    lambda message: not message.text.isdigit() or int(message.text) <= 0,
    state=ClientStatesGroup.amount_of_money,
)
async def check_amount_of_money(message: types.Message):
    print(f"Client {message.from_user.id} on {check_amount_of_money} put {message.text}")
    await message.reply("Некоректна сума вкладу!")


@dp.message_handler(
    lambda message: not message.text.isdigit() or int(message.text) < 3,
    state=ClientStatesGroup.amount_of_mounths,
)
async def check_amount_of_mounths(message: types.Message):
    print(f"Client {message.from_user.id} on {check_amount_of_mounths} put {message.text}")
    await message.reply("Некоректні дані!")


@dp.message_handler(state=ClientStatesGroup.amount_of_money)
async def amount_of_money(message: types.Message, state: FSMContext):
    print(f"Client {message.from_user.id} on amount_of_money")
    async with state.proxy() as data:
        data["amount_of_money"] = int(message.text)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://img.indiafilings.com/learn/wp-content/uploads/2016/06/12010651/loan-and-deposit.jpg",
    )
    await ClientStatesGroup.amount_of_mounths.set()
    await message.answer(
        "Мінімальний термін вкладу на 3 місяці\nРекомендований термін вкладу має бути кратним 3 місяцям."
    )
    await message.answer("Введіть на скільки місяців відкрити депозит:")


@dp.message_handler(state=ClientStatesGroup.amount_of_mounths)
async def amount_of_mounths(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data_deposit = my_wallet.manager_money(data["amount_of_money"], int(message.text))
        print(f"Client {message.from_user.id} try to calc manager_money {data['amount_of_money'], int(message.text)}")
    await message.answer("Зачекайте... проводиться розрахунок...")
    my_formatter = Formatter(data_deposit, message.chat.id)
    my_formatter.save_pdf()
    await bot.send_document(chat_id=message.chat.id, document=open(f"{message.chat.id}.pdf", "r+b"))
    await os.remove(f"{message.chat.id}.pdf")
    print(f"Client {message.from_user.id} get file")
    await BankGroup.privat.set()
    await message.answer("PrivatBank меню:", reply_markup=get_kb_PrivatBank())


@dp.message_handler(text=["MonoBank", "<== MonoBank"], state="*")
async def MonoBank(message: types.Message):
    print(f"Client {message.from_user.id} in MonoBank")
    await BankGroup.mono.set()
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://banki.ua/sites/default/files/monobank.png",
    )
    await message.answer("MonoBank меню:", reply_markup=get_kb_MonoBank())


@dp.message_handler(text="Курс $", state=BankGroup.mono)
async def MonoBank(message: types.Message):
    print(f"Client {message.from_user.id} in MonoBank exchange_rate")
    text = my_mono.exchange_rate()
    await message.answer(text, reply_markup=get_kb_back_mono())


if __name__ == "__main__":
    print("Bot has started work...")
    executor.start_polling(dp)
