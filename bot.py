import os
import time
import telebot
import schedule
import threading
from datetime import datetime, timedelta
from flask import Flask

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

def send_daily_forecast():
    tomorrow = datetime.now() + timedelta(days=1)
    message = f "Прогнозы на" {tomorrow.strftime('%d.%m.%Y')}:
1. Матч X - Победа за 1.95\n2. Матч Y - Тотал больше 2.5 за 1.75"
    bot.send_message(CHAT_ID, message)

# Планировщик
schedule.every().day.at("18:00").do(send_daily_forecast)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(10)

@app.route('/')
def home():
    return "Bot is running"

if __name__ == "__main__":
    t = threading.Thread(target=run_schedule)
    t.daemon = True
    t.start()
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
