import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.from_user.first_name
    await update.message.reply_text(f"مرحبا {name}!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    if msg == "السلام عليكم":
        await update.message.reply_text("وعليكم السلام")
    elif msg == "من انت":
        await update.message.reply_text("انا بوت ذكي صنعه عبدالملك 😄")
    elif msg == "مرحبا":
        await update.message.reply_text("اهلا وسهلا 👋")
    elif msg == "وداعا":
        await update.message.reply_text("مع السلامة! 👋 الى اللقاء")
    else:
        await update.message.reply_text("ما فهمت قصدك 😅 كيف حالك؟ جرب تكتب:")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot is running!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
