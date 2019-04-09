import telebot
from telebot import types
from key import key
import requests
import os
import re
bot = telebot.TeleBot(key)


def inline_key(num):
    """Функция для вывода кнопок
    """
    i=1
    btns = []
    while i<=num:
        btns.append(types.InlineKeyboardButton(text='Кнопка '+str(i+10), callback_data='butt'+str(i+10)))
        i=i+1
    btns.append(types.InlineKeyboardButton(text='назад', callback_data='nazad'))
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*btns)
    return keyboard

@bot.message_handler(commands=["start"])
#главное меню
def start(m):
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton(text='кнопка1', callback_data="butt1"))
    key.add(types.InlineKeyboardButton(text='кнопка2', callback_data="butt2"))
    msg=bot.send_message(m.chat.id, 'Нажми кнопку', reply_markup=key)



@bot.callback_query_handler(func=lambda call: True)
def inline(c):

    if c.data=='butt1':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="нажата *кнопка 1*",
            parse_mode="markdown")
    elif c.data=='butt2':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="нажата *кнопка 2*",
            parse_mode="markdown",
            reply_markup=inline_key(5))
    elif c.data=='nazad':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="нажата *кнопка 2*",
            parse_mode="markdown",
            reply_markup=inline_key(2))


if __name__ == "__main__":
    bot.polling(none_stop=True)