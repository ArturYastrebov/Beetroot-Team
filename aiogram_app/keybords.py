from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def subscribers_keyboard() -> InlineKeyboardMarkup:
    subscr_menu = InlineKeyboardMarkup(row_width=2)
    btn_subscr = InlineKeyboardButton(text='subscribe', callback_data='cd_btn_subscr')
    btn_unsubscr = InlineKeyboardButton(text='unsubscribe', callback_data='cd_btn_unsubscr')
    subscr_menu.insert(btn_subscr)
    subscr_menu.insert(btn_unsubscr)
    return subscr_menu
