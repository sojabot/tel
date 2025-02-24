import requests
import time
from bs4 import BeautifulSoup

# توکن و آیدی کانال
BOT_TOKEN = "7838503399:AAFkfktShHKS8-sun8WvM2Xi1Bnxpe2i9Vk"
CHANNEL_ID = "@malacointt"

# URL سایت موردنظر
URL = "https://www.kanoonnews.ir/"

def get_text_from_website():
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
             ##box2 > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)
            element = soup.select_one("#box2 > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)")
            
            if element:
                return element.text.strip() # گرفتن متن اولین خبر
            else:
                return "❌ خبری در صفحه پیدا نشد."
        else:
            return f"❌ خطا در دریافت صفحه: {response.status_code}"
    except Exception as e:
        return f"❌ خطای غیرمنتظره: {str(e)}"

def send_message_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": message}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("✅ پیام با موفقیت ارسال شد!")
    else:
        print("❌ خطا در ارسال پیام:", response.json())

# اجرای ربات هر 10 ثانیه
while True:
    text = get_text_from_website()
    send_message_to_telegram(text)
    time.sleep(10)
