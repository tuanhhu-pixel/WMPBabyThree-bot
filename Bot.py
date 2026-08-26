import os
import threading

from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


# =========================
# WEB SERVER FOR RENDER
# =========================

web_app = Flask(__name__)


@web_app.route("/")
def home():
    return "Team Assistant Bot is running!", 200


def run_web_server():
    port = int(os.environ.get("PORT", 10000))

    web_app.run(
        host="0.0.0.0",
        port=port,
        use_reloader=False
    )


# =========================
# TELEGRAM BOT
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Xin chào!\n\n"
        "Tôi là Team Assistant Bot.\n"
        "Bot đã kết nối thành công."
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 Bot đang hoạt động!"
    )


# =========================
# MAIN
# =========================

def main():

    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("Chưa cấu hình BOT_TOKEN")

    # Start web server
    web_thread = threading.Thread(
        target=run_web_server,
        daemon=True
    )

    web_thread.start()

    # Start Telegram bot
    app = Application.builder().token(token).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("ping", ping)
    )

    print("Telegram Bot đang chạy...")

    app.run_polling()


if __name__ == "__main__":
    main()
