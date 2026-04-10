from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я работаю на Render!")

def main():
    # Берём токен из переменной окружения
    token = os.getenv("TG_TOKEN")

    app = ApplicationBuilder().token(token).build()

    # Регистрируем команду
    app.add_handler(CommandHandler("start", start))

    # Запуск (БЕЗ asyncio.run !!!)
    app.run_polling()

if __name__ == "__main__":
    main()
