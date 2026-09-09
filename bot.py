import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 🤖\n"
        "ربات با موفقیت روشنه!\n\n"
        "دستور /help رو بفرست."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 راهنما\n\n"
        "/start - شروع ربات\n"
        "/help - راهنما"
    )

TOKEN = os.getenv("BOT_TOKEN")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()