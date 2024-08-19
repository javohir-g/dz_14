from telebot import types

def button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    usd_to_uzs_btn = types.KeyboardButton('USD ➡️ UZS')
    uzs_to_usd_btn = types.KeyboardButton('UZS ➡️ USD')
    kb.add(usd_to_uzs_btn, uzs_to_usd_btn)
    return kb