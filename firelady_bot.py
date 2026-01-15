# firelady_bot.py
import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

MY_BOT_TOKEN = os.getenv('MY_BOT_TOKEN')
bot = telebot.TeleBot(MY_BOT_TOKEN)

#  Перевірка токена
if not MY_BOT_TOKEN:
    raise ValueError("MY_BOT_TOKEN is not set in .env")

# Функції клавіатури
def get_yes_no_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Так ✅", callback_data="yes"),
        types.InlineKeyboardButton("Ні ❌", callback_data="no")
    )
    return markup

def get_instagram_and_site_markup():
    markup = types.InlineKeyboardMarkup()
    btn_inst = types.InlineKeyboardButton('Перейти в Instagram 🔗', url='https://www.instagram.com/ivanovyshki?igsh=ZjdvM241bDV1NW9o')
    btn_site = types.InlineKeyboardButton('Перейти на сайт 🌐', url='https://homemadecandle.onrender.com/'
    )
    markup.add(btn_inst, btn_site)
    return markup

@bot.message_handler(commands=['fire'])
def handle_fire(message):
    markup = get_yes_no_markup()
    bot.send_message(message.chat.id, "Hello 👋. Я  Fire Lady. "
                                      "Виготовлення формових свічок - це моя справа. "
                                      "Хочеш дізнатися про це більше? Тисни ТАК",
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "yes")
def callback_yes(call):
    markup = get_instagram_and_site_markup()
    bot.send_message(call.message.chat.id, """🔥 Формові свічки — це справжнє поєднання ремесла й мистецтва 🕯️✨
Це свічки, які заливаються у спеціальні форми (зазвичай силіконові), щоб отримати унікальні фігури: від класичних колон до фігурок людей, тварин, квітів чи навіть абстрактних скульптур. Вони можуть бути як декоративними, так і функціональними.
Що робить формові свічки особливими:
- Індивідуальний дизайн — кожна форма дозволяє створити щось унікальне: наприклад, свічку у вигляді жіночого тіла, ведмедика, серця чи ялинки.
- Матеріали — часто використовують натуральний соєвий або бджолиний віск, що робить їх екологічними та безпечними.
- Ручна робота — більшість таких свічок виготовляються вручну, з увагою до деталей, що додає їм естетичної цінності.
- Подарунковий потенціал — вони чудово підходять як подарунок або елемент декору.
Майстерні на кшталт Palala чи 5candles пропонують не лише готові свічки, а й форми, матеріали та навіть навчання для тих, хто хоче створювати власні шедеври.
Хочеш, я допоможу тобі підібрати форму або створити опис для твоєї власної колекції свічок? 🔥🕯️
Ось посилання на каталог в Instagram та сайт 
""",
    reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "no")
def callback_no(call):
    bot.send_message(call.message.chat.id, "👌 Без проблем! Я завжди поруч.")

bot.infinity_polling()
