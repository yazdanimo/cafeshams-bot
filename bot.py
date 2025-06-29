
import os
import time
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
INTERVAL = int(os.getenv("INTERVAL_SECONDS", 15))

bot = Bot(BOT_TOKEN)

def fetch_news():
    # فقط یک نمونه ساده
    return [{"id": str(int(time.time())), "text": "📰 خبر تستی کافه شمس | " + time.strftime("%H:%M:%S")}]

sent_ids = set()

while True:
    news = fetch_news()
    for item in news:
        if item['id'] not in sent_ids:
            bot.send_message(chat_id=CHAT_ID, text=item['text'])
            sent_ids.add(item['id'])
    time.sleep(INTERVAL)
