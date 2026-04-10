import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я работаю на Render!")

async def main():
    # Берём токен из переменной окружения TG_TOKEN
    token = os.getenv("TG_TOKEN")

    if not token:
        raise ValueError("❌ Ошибка: переменная окружения TG_TOKEN не найдена!")

    # Создаем приложение бота
    app = ApplicationBuilder().token(token).build()

    # Регистрируем обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    # Запускаем опрос Telegram
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
