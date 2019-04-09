import telebot
from telebot import types
from key import key
import requests
import os
bot = telebot.TeleBot(key)

thunderstorm = u'\U0001F4A8'    # Code: 200's, 900, 901, 902, 905
breeze = u'\U0001F4A8'
drizzle = u'\U0001F601'         # Code: 300's
rain = u'\U00002614'            # Code: 500's
snowflake = u'\U00002744'       # Code: 600's snowflake
snowman = u'\U000026C4'         # Code: 600's snowman, 903, 906
atmosphere = u'\U0001F301'      # Code: 700's foogy
clearSky = u'\U00002600'        # Code: 800 clear sky
fewClouds = u'\U000026C5'       # Code: 801 sun behind clouds
clouds = u'\U00002601'          # Code: 802-803-804 clouds general
hot = u'\U0001F525'             # Code: 904
sparcle = u'\U00002728' # default emojis
hi = u'\U0001F64B'



@bot.message_handler(commands=['start'])
def handle_start_help(message):

        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('/Каталог', 'О нас', 'Хочу сделать заказ')
        user_markup.row('Наши акции')
        bot.send_message(message.chat.id,'Привет!' + hi + 'На связи Qol_Decor!' + '\n'
                                        'Это моя виртуальная помощница Яна ' 
                                        'она поможет вам украсить ваш дом или офис '
                                        'декоративными изделиями ручной работы' + sparcle , reply_markup=user_markup)

        MethodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates?offset=10'.format(token=key)

        response = requests.post(MethodGetUpdates)
        result = response.json()
        print(result)


@bot.message_handler(commands=['Каталог'])
def send_photo(message):
    if message.text == '/Каталог':
        # directory = 'img/coffe.jpg'
        # img = open(directory, 'rb')
        bot.send_message(message.chat.id, 'Представляем вам наш каталог!' + sparcle)
        # bot.send_photo(message.chat.id, img )
        # img.close()
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Чайные домики', 'Кофейные столики', 'Светильники')
        user_markup.row('хочу заказать')
        if message.text == 'F':
            bot.send_message(message.chat.id, 'CYKA')
        bot.send_message(message.chat.id,'.', reply_markup=user_markup)



@bot.message_handler(content_types=['text'])
def command_1(message):
    if message.text == 'Чайные домики':
        directory = 'img/home'
        all_file = os.listdir(directory)
        print(all_file)
        for file in all_file:
            img = open(directory + '/' + file, 'rb')
            bot.send_photo(message.chat.id, img)
            img.close()
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Чайные домики', 'Кофейные столики', 'Светильники')
        user_markup.row('хочу заказать')
        bot.send_message(message.chat.id,'Здесь представленно'
                                         ' несколько Чайных'
                                         ' домиков!!!' , reply_markup=user_markup)

    elif message.text == 'Кофейные столики':
        directory = 'img/table'
        all_file = os.listdir(directory)
        print(all_file)
        for file in all_file:
            img = open(directory + '/' + file, 'rb')
            bot.send_photo(message.chat.id, img)
            img.close()
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Чайные домики', 'Кофейные столики', 'Светильники')
        user_markup.row('хочу заказать')
        bot.send_message(message.chat.id, 'Здесь представленно'
                                          ' несколько кофейных столиков', reply_markup=user_markup)

    elif message.text == 'О нас':
        video = open('video/1.mp3', 'rb')
        bot.send_video(message.chat.id, video)
        video.close()
    elif message.text == 'хочу заказать':
        bot.send_message(message.chat.id, "Введите ваши данные а так же номер заказа пример:Иванов Иван,"
                                          "Ул.Пушкина Кв. 7, 88005553535,а111111 (номер заказа), наш курьер"
                                          " свяжеться с вами для уточнения деталей заказа")

        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('По интернету', 'При получении')
        bot.send_message(message.chat.id,'Выберите способы оплаты', reply_markup=user_markup)

    elif message.text == 'При получении':
        bot.send_message(message.chat.id, "Спасибо за заказ наш"
                                          " курье в ближайшее время свяжеться с вами для уточнения заказа")

    elif message.text == '4':
        bot.send_message(message.chat.id, message.chat.id)
        print(message.chat.id) #этот идентификатор будет записываться как уникальной и потом летит в базу вместе с ним
    else:
        echo_msg(message) #тут используем функцию



@bot.message_handler(func=lambda message: True,content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text) # здесь он отправляеть сообщение (What??) на наш телеграмм бот
    print(message.text)
    markup = types.ReplyKeyboardRemove(True)
    bot.send_message(message.chat.id, "Простите я непонял ваш вопрос :" + str(message.text), reply_markup=markup)



if __name__ == '__main__':
    bot.polling(none_stop=True)