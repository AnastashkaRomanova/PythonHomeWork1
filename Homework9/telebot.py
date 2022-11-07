from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from bot_command import hello

from bot_command import calculater
# import telebot
# from bot_command import send_text
    


app = ApplicationBuilder().token("5355352008:AAGpdjKisE0wLZPTzG9Mrw6i-NBQlRcDR3s").build()

app.add_handler(CommandHandler("hello", hello))
# app.add_handler(MessageHandler(filters.TEXT, send_text))
app.add_handler(CommandHandler('go', calculater))
print('serv start)')

app.run_polling()