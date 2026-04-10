from telegram.ext import Application, CommandHandler
import os

async def start(update, context):
    await update.message.reply_text("Бот работает!")

def main():
    token = os.getenv("TG_TOKEN")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()   # <<< БЕЗ await и БЕЗ asyncio.run

if __name__ == "__main__":
    main()
