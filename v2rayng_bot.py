from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# اطلاعات API پنل V2RayNG
API_URL = "http://your-v2ray-panel-url/api"
API_TOKEN = "your-panel-api-token"

# ایجاد اکانت تست
def create_test_account():
    payload = {
        "action": "create_user",
        "token": API_TOKEN,
        "username": "test_user",
        "expire": "1d"  # مدت زمان اعتبار اکانت
    }
    try:
        response = requests.post(f"{API_URL}/create_user", json=payload)
        if response.status_code == 200:
            data = response.json()
            return f"اکانت تست شما:\n\n{data.get('link')}"
        else:
            return "مشکلی در ساخت اکانت تست پیش آمده است."
    except Exception as e:
        return f"خطا: {e}"

# دستور /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("به ربات V2Ray خوش آمدید! برای دریافت اکانت تست، دستور /test را ارسال کنید.")

# دستور /test
def test(update: Update, context: CallbackContext) -> None:
    account_info = create_test_account()
    update.message.reply_text(account_info)

def main():
    # توکن ربات تلگرام
    TELEGRAM_TOKEN = "your-telegram-bot-token"

    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    # ثبت دستورات
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("test", test))

    # اجرای ربات
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
