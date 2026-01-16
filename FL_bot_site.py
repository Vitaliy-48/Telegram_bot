import telebot, os
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
MY_BOT_TOKEN = os.getenv('MY_BOT_TOKEN')
botFL = telebot.TeleBot(MY_BOT_TOKEN)



@botFL.message_handler(commands=['fire'])
def start(message):
    botFL.send_message(message.chat.id, 'Hello. Im Fire. What is your name?')
    botFL.register_next_step_handler(message, ask_name)

def ask_name(message):
    user_name = message.text
    botFL.send_message(message.chat.id, f"Nice to meet you, {user_name}! 😊")
    botFL.send_message(message.chat.id, 'Ось невеличка презентація')
    # Після відповіді показуємо каталог фото
    send_photo(message)
    botFL.send_message(message.chat.id, 'Маєш бажання дізнатися більше?')
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Так', callback_data='yes')
    markup.add(button_yes)
    # Відправляємо повідомлення з кнопкою
    botFL.send_message(message.chat.id, "Натисни кнопку нижче 👇", reply_markup=markup)


def send_photo(message):
    photos = os.listdir('images')
    photos = [f for f in photos if f.lower().endswith(('.jpg', 'jpeg', 'png', 'webp', 'gif'))]
    if not photos:
        botFL.send_message(message.chat.id, 'У каталозі images немає зображень.')

    for photo_path in photos:
        with open(os.path.join("images", photo_path), "rb") as photo:
            botFL.send_photo(message.chat.id, photo, caption=f'Фото: {photo_path}')


@botFL.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Виготовлення формових свічок - це моя справа.\nЩоб побачити  більше переглянь сторінку"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://homemadecandle.onrender.com/"))
        botFL.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botFL.answer_callback_query(function_call.id)


botFL.polling()