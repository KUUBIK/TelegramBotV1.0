import telebot
from telebot import types
import datetime
from key import key
import requests

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
        user_markup.row('/start', '/фоточка', '/testing_mode')
        user_markup.row('/видосик', '/аудюшка')
        bot.send_message(message.chat.id,'Дратути', reply_markup=user_markup)

        MethodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates?offset=10'.format(token=key)

        response = requests.post(MethodGetUpdates)
        result = response.json()
        print(result)


@bot.message_handler(commands=['фоточка'])
def send_photo(message):
    if message.text == '/фоточка':
        directory = 'img/1.png'
        img = open(directory, 'rb')
        bot.send_message(message.chat.id, 'load photos!')
        bot.send_photo(message.chat.id, img)
        img.close()


@bot.message_handler(commands=['видосик'])
def send_video(message):
   if message.text == '/видосик':
        dir = 'video/1.mp3'
        video = open(dir, 'rb')
        bot.send_message(message.chat.id, 'load video!')
        bot.send_video(message.chat.id, video)
        video.close()


@bot.message_handler(commands=['аудюшка'])
def send_audio(message):
    if message.text == '/аудюшка':
        dir = 'audio/1.mp3'
        video = open(dir, 'rb')
        bot.send_message(message.chat.id, 'load video!')
        bot.send_video(message.chat.id, video)
        video.close()




@bot.message_handler(commands=['testing_mode'])
def testing_mode(message):
    bot.send_message(message.chat.id, "Приветствую мы компания занимающаяс продажей воздуха!!!"

                     )
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('1', '2', '3', '4')
    bot.send_message(message.chat.id,   "1.Почему мы?" + "\n"
                                        "2.Зачем это вам?" +"\n"
                                        "3.Чем мы лучше?" + "\n"
                                        "4.Немного о самой компании", reply_markup=user_markup)



@bot.message_handler(content_types=['text'])
def command_1(message):
    if message.text == '1':
        bot.send_message(message.chat.id, 'congratulations!!1')
    elif message.text == '2':
        bot.send_message(message.chat.id, 'congratulations!!2')
    elif message.text == '3':
        bot.send_message(message.chat.id, 'congratulations!!3')
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


