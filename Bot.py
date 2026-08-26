import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Xin chào!\n\n"
        "Tôi là Team Assistant Bot.\n"
        "Bot đã kết nối thành công."
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Bot đang hoạt động!")


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("Chưa cấu hình BOT_TOKEN")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))

    print("Bot đang chạy...")
    app.run_polling()


if __name__ == "__main__":
    main()
