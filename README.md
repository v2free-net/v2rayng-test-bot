# v2rayng-test-bot
**اکانت تست V2RayNG** را به‌راحتی از طریق ربات تلگرام دریافت کنید. این ربات به شما امکان می‌دهد بدون نیاز به تنظیمات پیچیده، اکانت تست سریع و معتبر دریافت کنید.

**معرفی ربات تلگرام برای اکانت تست V2RayNG**

ما با ایجاد ربات تلگرام **V2RayNG Test Account**، فرآیند دریافت اکانت تست را ساده و سریع کرده‌ایم. کاربران می‌توانند تنها با ارسال یک دستور، اکانت تست خود را دریافت کنند و از امکانات این سرویس به راحتی بهره‌مند شوند. این ربات به‌ویژه برای کسانی که به‌دنبال آزمایش قابلیت‌های **V2RayNG** هستند، یک راه حل ایده‌آل است.

برای مشاهده نمونه و دریافت اکانت تست v2rayng از ربات، روی لینک زیر کلیک کنید:

###  [ربات تلگرام نمونه](https://t.me/v2makers_free_bot)

---

### آموزش کامل ساخت ربات تلگرام برای اکانت تست V2RayNG

در این آموزش، نحوه ساخت ربات تلگرام برای اتصال به پنل **V2RayNG** و ایجاد اکانت تست به همراه متن نمونه کار برای معرفی ربات توضیح داده می‌شود. با استفاده از این ربات، کاربران می‌توانند به‌راحتی و بدون نیاز به تنظیمات پیچیده، اکانت تست V2RayNG خود را دریافت کنند.

---

### مرحله ۱: دریافت توکن ربات تلگرام
1. به **BotFather** در تلگرام مراجعه کنید.
2. دستور `/newbot` را وارد کرده و مراحل ایجاد ربات را طی کنید.
3. در انتها توکن ربات خود را دریافت خواهید کرد که برای ارتباط با ربات از آن استفاده خواهید کرد.

---

### مرحله ۲: آماده‌سازی محیط
1. در سرور خود Python را نصب کنید (اگر هنوز نصب نکرده‌اید).
2. کتابخانه‌های لازم را نصب کنید:
   ```bash
   pip install python-telegram-bot requests
   ```

---

### مرحله ۳: کدنویسی ربات

در این مرحله، کد زیر را برای ساخت ربات تلگرام و اتصال به پنل **V2RayNG** به یک فایل پایتون (مثلاً `v2rayng_bot.py`) ذخیره کنید:

```python
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
```

در کد بالا:
- اطلاعات مربوط به API پنل **V2RayNG** خود را وارد کنید (آدرس URL و توکن).
- توکن ربات تلگرام خود را در قسمت `TELEGRAM_TOKEN` قرار دهید.

---

### مرحله ۴: اجرای ربات
1. پس از ذخیره کد، فایل پایتون را اجرا کنید:
   ```bash
   python v2rayng_bot.py
   ```
2. ربات شما آماده است و می‌توانید از طریق تلگرام به آن متصل شوید.

---

### مرحله ۵: تست ربات
- در تلگرام به ربات خود پیام دهید و دستور `/start` یا `/test` را ارسال کنید.
- ربات باید یک لینک اکانت تست V2RayNG به شما ارسال کند.

---

### این ربات به شما کمک می‌کند تا فرآیند ارائه اکانت‌های تست V2RayNG را به روشی ساده و خودکار انجام دهید. با این روش، کاربران به سرعت می‌توانند از سرویس‌های V2RayNG بهره‌مند شوند و بدون نیاز به انجام تنظیمات پیچیده، سرویس‌های خود را تست کنند.
