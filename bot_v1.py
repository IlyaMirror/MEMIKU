import telebot
from telebot import types
import numpy as np
import pandas as pd
import random

bot = telebot.TeleBot('5511739630:AAH4XYAW3tuxcPpy3URJLir3o804G_GdvDY')
movies = pd.read_excel('Movies_1.xlsx')
series = pd.read_excel('Series_1.xlsx')


npdata_m = np.array(movies)
npdata_s = np.array(series)

def rand_movies():
    r = random.randint(0, 9)
    name = (npdata_m[r] [:1])
    year = (npdata_m[r] [1:2])
    rating = (npdata_m[r] [2:3])
    description = (npdata_m[r] [4:5])
    return name, year, rating, description


def rand_series():
    r = random.randint(0, 8)
    name = (npdata_s[r] [:1])
    year = (npdata_s[r] [1:2])
    rating = (npdata_s[r] [2:3])
    description = (npdata_s[r] [4:5])
    return name, year, rating, description



@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🎬 Кино')
    item2 = types.KeyboardButton('🎞 Сериал')
    item3 = types.KeyboardButton('🍑 Аниме')
    item4 = types.KeyboardButton('🦊 О нас')

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}!'.format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🎬 Кино':
            name_m, year_m, rating_m, descrip_m = rand_movies()
            bot.send_message(message.chat.id,
                             ('Название: ' + str(*name_m)
                              + '\n' + 'Год: ' + str(*year_m)
                              + '\n' + 'Рейтинг: ' + str(*rating_m)
                              + '\n' + '\n' + 'Синопсис: '
                              + str(*descrip_m)))
        elif message.text == '🎞 Сериал':
            name_s, year_s, rating_s, descrip_s = rand_series()
            bot.send_message(message.chat.id,
                             ('Название: ' + str(*name_s)
                              + '\n' + 'Год: ' + str(*year_s)
                              + '\n' + 'Рейтинг: ' + str(*rating_s)
                              + '\n' + '\n' + 'Синопсис: '
                              + str(*descrip_s)))




bot.polling(none_stop=True)