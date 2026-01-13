# 🔥 Telegram Bot — Fire Lady

Цей репозиторій містить кілька Telegram-ботів, які презентують хендмейд-свічки, надсилають фото, та ведуть користувача до Instagram або локального сайту.

## 📦 Структура проєкту
├── .env                  # Зберігає токен бота (MY_BOT_TOKEN) 
├── .gitignore            
├── firelady_bot.py       # Основний бот з командою /fire та описом свічок 
├── FL_bot_ins.py         # Бот з кнопкою переходу в Instagram 
├── FL_bot_site.py        # Бот з кнопкою переходу на локальний сайт 
├── fire3_FL_bot.jpg      # Зображення, яке надсилається ботом 
├── requirements.txt      # Залежності (створити через pip freeze) 
└── .venv/                # Віртуальне середовище (ігнорується Git)


## 🚀 Як запустити

1. **Клонувати репозиторій**
   ```bash
   https://github.com/Vitalii-48/Telegram_bot
2. **Створити віртуальне середовище** 
  python -m venv .venv
  .venv\Scripts\activate  # Windows
3. **Встановити залежності**
  pip install -r requirements.txt
4. **Створтит файл .env**
  MY_BOT_TOKEN = "тут_твій_токен"
5. **Запустити потрібний бот**
  python firelady_bot.py

## 🧠 Функціонал
- /fire — надсилає опис формових свічок та кнопки "Так" / "Ні".
- При натисканні "Так" — надсилає текст з описом і кнопку переходу в Instagram.
- /photo — надсилає зображення fire3_FL_bot.jpg.
- Відповідає на будь-яке повідомлення з фото і кнопкою "Так".
- Переходи: Instagram або сайт HomeMadeCandle(https://homemadecandle.onrender.com/).

## ⚙️ Залежності
requirements.txt
- pyTelegramBotAPI==4.15.4
- python-dotenv==1.0.1

## 👩‍💻 Авторство
Проєкт за допомогою штучного інтелекту (Microsoft Copilot).