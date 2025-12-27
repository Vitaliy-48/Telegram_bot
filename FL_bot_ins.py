import telebot
from dotenv import load_dotenv
import os

load_dotenv()
MY_BOT_TOKEN = os.getenv('MY_BOT_TOKEN')



botFL = telebot.TeleBot(MY_BOT_TOKEN)
from telebot import types

@botFL.message_handler(commands=['start'])
def start(message):
    botFL.send_message(message, 'Hello')
    botFL.reply_to(message, 'Hello')

@botFL.message_handler(commands=['photo'])
def send_photo(message):
    with open("fire.jpg", "rb") as photo:
        botFL.send_photo(message.chat.id, photo, caption="Ось ваше зображення!")


@botFL.message_handler(func=lambda message: True)
def echo_all(message):
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Так', callback_data='yes')
    markup.add(button_yes)
    # Відправляємо зображення перед текстом
    with open("fire3_FL_bot.jpg", "rb") as photo:  # Замініть "image.jpg" на вашу картинку
        botFL.send_photo(message.chat.id, photo)

    botFL.send_message(message.chat.id, message.text + ' Хочеш знати хто така Fire Lady?\nНажми    Так', reply_markup=markup)


@botFL.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Виготовлення формових свічок - це моя справа.\nЩоб побачити  більше переглянь сторінку"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сторінку", url="https://www.instagram.com/ivanovyshki?igsh=ZjdvM241bDV1NW9o"))
        botFL.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botFL.answer_callback_query(function_call.id)

botFL.polling()