import telebot
from datetime import datetime
from telebot import types
token = '485606860:AAFC1eSP_LksyJSRHsDK0Z9b49Rt4u_YzEI'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def get_time_now():
    return datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')

def write_to_log(who,text):
    file = open('log.txt','a+',encoding = 'utf-8')
    file.write(' '+str(who)+' '+ str(text)+'\n')
    file.close()

def start(message):
        bot.send_message(message.chat.id, 'Hi')
        #write_to_log(message.from_user.id,'Пользователь начал использовать бота')
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
        bot.register_next_step_handler(message,choice_user)

def choise_user(message):
    if message.text == 'Узнать слово':
        write_to_log(message.from_user.id,'Пользатель выбрал "узнать слово"')
        bot.send_message(message.from_user.id,'Введите слово: ')
        bot.register_next_step_handler(message, search_word)
bot.polling(none_stop=True)
