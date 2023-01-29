from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiofiles import os

from data_parser import parser_items, get_category_menu, get_ikea_category_data, \
    COMMAND_CATEGORY_MENU
from formatter import formatter_menu, FORMATTER_DICT

from config import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


class ClientStatesGroup(StatesGroup):
    category = State()
    sub_category = State()
    type_formatter = State()


def get_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("/cancel"))
    return kb


@dp.message_handler(commands="cancel", state="*")
async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Enter /start if you want to pars the IKEA shop")


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Ikea_logo.svg/" "1280px-Ikea_logo.svg.png",
    )
    await message.answer("Welcome to IKEA pars bot\nSelect the number of category you want to parse\n")
    print(f"{message.from_user.id} on category menu")
    category_menu = get_category_menu()
    await bot.send_message(chat_id=message.from_user.id, text=category_menu)
    await ClientStatesGroup.category.set()


@dp.message_handler(
    lambda message: message.text in str(list(COMMAND_CATEGORY_MENU.keys())) and message.text != "0",
    state=ClientStatesGroup.category,
)
async def category_handler(message: types.Message, state: FSMContext):
    ikea_data = get_ikea_category_data()
    if message.text[:1] != "/":
        message.text = "/" + message.text
    async with state.proxy() as data:
        data["category"] = COMMAND_CATEGORY_MENU[message.text]
    await message.answer(f"You have selected the {COMMAND_CATEGORY_MENU[message.text]} category")
    await message.answer(f"Select a subcategory to parse")
    answer_data = ""
    for index, category in enumerate(ikea_data[COMMAND_CATEGORY_MENU[message.text]], start=1):
        answer_data += f"/{index}" + " - " + category.get("title") + "\n"
    print(f"{message.from_user.id} on sub_category menu")
    await message.answer(answer_data, reply_markup=get_cancel())
    await ClientStatesGroup.next()


@dp.message_handler(lambda message: message.text, state=ClientStatesGroup.sub_category)
async def sub_category_handler(message: types.Message, state: FSMContext):
    if message.text[:1] != "/":
        message.text = "/" + message.text
    async with state.proxy() as data:
        ikea_data = get_ikea_category_data()
        data["sub_category"] = ikea_data[data["category"]][int(message.text[1:]) - 1]
        await message.answer(f'You have selected the {data["sub_category"]["title"]} subcategory')
    await message.answer(f"Select the format for saving the result")
    answer_data = ""
    formatter_menu_list = formatter_menu(FORMATTER_DICT)
    for formatter_data in formatter_menu_list:
        answer_data += f"/{formatter_data[0]}" + " - " + formatter_data[1] + "\n"
    print(f"{message.from_user.id} on type_formatter menu")
    await message.answer(answer_data, reply_markup=get_cancel())
    await ClientStatesGroup.next()


@dp.message_handler(lambda message: message.text, state=ClientStatesGroup.type_formatter)
async def type_formatter(message: types.Message, state: FSMContext):
    if message.text[:1] != "/":
        message.text = "/" + message.text
    await message.answer(f"Start parsing...please wait")
    async with state.proxy() as data:
        formatter_menu_list = formatter_menu(FORMATTER_DICT)
        data["type_formatter"] = formatter_menu_list[int(message.text[1:]) - 1][1]
        print(f"{message.chat.id} try to pars in {data['type_formatter']}")
        pars_data, title = parser_items(data["sub_category"])
        if data["type_formatter"] in ["csv"]:
            await FORMATTER_DICT[data["type_formatter"]](pars_data, title)
        else:
            FORMATTER_DICT[data["type_formatter"]](pars_data, title)
        await message.answer(f'Data was saved to file {title}.{data["type_formatter"]}')
        await bot.send_document(chat_id=message.chat.id, document=open(f'{title}.{data["type_formatter"]}', "r+b"))
        print(f"{message.chat.id} got file in {title}.{data['type_formatter']}")
        await os.remove(f'{title}.{data["type_formatter"]}')
        await state.finish()
        await message.answer("Enter /start if you want to pars the IKEA shop again")


if __name__ == "__main__":
    print("Bot has started work...")
    executor.start_polling(dp)
