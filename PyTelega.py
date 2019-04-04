import telebot
from telebot import types
import datetime
from key import key


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
defaultEmoji = u'\U0001F300' # default emojis
nail = u'\U0001F485'


@bot.message_handler(commands=['start'])
def handle_start_help(message):

        bot.send_message(message.chat.id, 'Привет! я тестовый бот по' + '\n'
                                          'ноготочкам!!!' + nail +
                                            'выберите себе ноготочки'
                         )
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('/start', '/фоточка')
        user_markup.row('/видосик', '/аудюшка')
        bot.send_message(message.chat.id,'Дратути', reply_markup=user_markup)


@bot.message_handler(commands=['фоточка'])
def send_photo(message):
    if message.text == '/фоточка':
        directory = 'img/1.png'
        img = open(directory, 'rb')
        bot.send_message(message.chat.id, 'load photos!')
        bot.send_photo(message.chat.id, img)



@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, 'Погода билять!')


@bot.message_handler(func=lambda message: True,commands=['reverse'])
def reverseMessage(message):
    bot.send_message(message.chat.id, message.text)




@bot.message_handler(func=lambda message: True,commands=['time'])
def time(message):
    # listZvonok = ['8:00','9:05' ,'10:10' ,'11:15' ,'12:20' ,'13:25' ,'14:30', '15:35', '16:40', '17:45', '18:50' ]

    listZvonok = ['8:50','9:55' ,'11:10' ,'12:05' ,'13:10' ,'14:15' ,'15:20', '16:25', '17:30', '18:35', '19:40' ]
    nowHour = datetime.datetime.now()
    Hours = nowHour.hour
    # print(Hours)
    Hours = Hours - 8
    try:
        minute = listZvonok[Hours]
        minute = 'Пара заканчиваться в ' + str(minute)
        bot.send_message(message.chat.id, minute)
    except IndexError:
        bot.send_message(message.chat.id, 'Time is not difined!')


@bot.message_handler(func=lambda message: True,content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text) # здесь он отправляеть сообщение (What??) на наш телеграмм бот
    # print(message.text)
    markup = types.ReplyKeyboardRemove(True)
    bot.send_message(message.chat.id, "Choose one letter:" + str(message.text), reply_markup=markup)



if __name__ == '__main__':
    bot.polling(none_stop=True)


