# 🔥 Telegram Bot — Fire Lady

This repository contains several Telegram bots that showcase handmade candles, send photos, and guide users to Instagram or a local website.

## 📦 Project Structure
```
├── .gitignore            # Ignores .venv, .env, and other service files
├── fire3_FL_bot.jpg      # Image sent by the bot 
├── firelady_bot.py       # Main bot with /fire command and candle descriptions 
├── FL_bot_ins.py         # Bot with a button linking to Instagram 
├── FL_bot_site.py        # Bot with a button linking to the website 
├── Procfile              # Instructions for Render: how to run the bot
├── README.md             # Project documentation
├── requirements.txt      # Dependencies (generated via pip freeze) 
└── .venv/                # Virtual environment (ignored by Git)

```

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   https://github.com/Vitalii-48/Telegram_bot
2. **Create a virtual environment** 
  python -m venv .venv
  .venv\Scripts\activate  # Windows
3. **Install dependencies**
  pip install -r requirements.txt
4. **Create the .env file**
  MY_BOT_TOKEN = "тут_твій_токен"
5. **Run the desired bot**
  python firelady_bot.py

## 🧠 Functionality
/fire — sends a description of shaped candles and buttons "Yes" / "No".
When "Yes" is pressed — sends text with description and a button linking to Instagram.
/photo — sends the image fire3_FL_bot.jpg.
Responds to any message with a photo and "Yes" button.
Redirects: Instagram or website HomeMadeCandle.

## ⚙️ Dependencies
requirements.txt
pyTelegramBotAPI==4.15.4
python-dotenv==1.0.1

## 👩‍💻 Author
Project developed with the help of Artificial Intelligence (Microsoft Copilot).
