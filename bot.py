import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg and msg.document:
        if msg.document.file_name.lower().endswith(".pdf"):

            await context.bot.copy_message(
                chat_id=CHANNEL_ID,
                from_chat_id=msg.chat_id,
                message_id=msg.message_id
            )

            await context.bot.delete_message(
                chat_id=msg.chat_id,
                message_id=msg.message_id
            )

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.Document.ALL, handle_pdf))

app.run_polling()
