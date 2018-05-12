import telebot
from datetime import datetime
from telebot import types
import wikipedia
import requests
token = '485606860:AAFC1eSP_LksyJSRHsDK0Z9b49Rt4u_YzEI'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])




def start(message):
        bot.send_message(message.chat.id, 'Hi')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        fund_word_button = types.KeyboardButton('Узнать слово')
        keyboard.add(fund_word_button)
        
        translate_word_button = types.KeyboardButton('Перевести слово')
        keyboard.add(translate_word_button)
        
        kurs_valyut_button = types.KeyboardButton('Курс валют')
        keyboard.add(kurs_valyut_button)
        
        found_weather_button = types.KeyboardButton('Узнать погоду')
        keyboard.add(found_weather_button)
        bot.send_message(message.chat.id, 'Variant:', reply_markup=keyboard)
        bot.register_next_step_handler(message,choise_user)
        print(search_word)

def choise_user(message):
    if message.text == 'Узнать слово':
        #write_to_log(message.from_user.id,'Пользатель выбрал "узнать слово"')
        bot.send_message(message.from_user.id,'Введите слово: ')
        bot.register_next_step_handler(message, search_word)
    elif message.text == 'Перевести слово':
        bot.send_message(message.from_user.id,'Введите слово: ')
        bot.register_next_step_handler(message,translate_message)
    else:
        bot.register_next_step_handler(message,choise_user)




def translate_message(message):
    print('gggg')

    data = {'key': 'trnsl.1.1.20180428T041527Z.0bb0a0164e10fffa.105936f712da2811ffb3ddbd8f24d47a104a0ed3',
            'text': message.text,
            'lang':'ru-en',
            'format':'plain'}
    
    answer = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data=data).json()

    bot.send_message(message.from_user.id,answer['text'])
    bot.register_next_step_handler(message,choise_user)
    

def search_word(message):
    wikipedia.set_lang('ru')
    bot.send_message(message.from_user.id,wikipedia.summary(message.text))
    bot.register_next_step_handler(message,choise_user)



bot.polling(none_stop=True)
