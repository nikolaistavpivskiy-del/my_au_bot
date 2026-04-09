from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот работает.")

app = ApplicationBuilder().token("ТВОЙ_ТОКЕН_ЗДЕСЬ").build()

app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()
