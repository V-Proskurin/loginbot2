#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from config import *
from telebot import types
from telebot.types import ReplyKeyboardMarkup


bot = telebot.TeleBot(TOKEN)


def webAppKeyboardInline(): 
    keyboard = types.InlineKeyboardMarkup(row_width=1) 
    webApp = types.WebAppInfo("https://dev.x1team.ru/wp-admin/admin-ajax.php?action=wptelegram_login&source=WebAppData") # Переход на x1team, авторизация происходит в браузере телеграмм
    login_url = types.LoginUrl(url = "https://dev.x1team.ru/wp-admin/admin-ajax.php?action=wptelegram_login", request_write_access = True) # Авторизация через внешний браузер
    one = types.InlineKeyboardButton(text="Авторизация в telegram", web_app=webApp) 
    two = types.InlineKeyboardButton(text="Авторизация в браузере", login_url=login_url) 
    keyboard.add(one, two)  

    return keyboard  

@bot.message_handler(commands=['start'])  
def start_fun(message):
    bot.send_message(message.chat.id, 'Привет, ✌️")\nНажми на кнопки внизу.', parse_mode="Markdown",
                     reply_markup=webAppKeyboardInline()) 



bot.infinity_polling()
