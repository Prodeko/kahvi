import os
from dotenv import load_dotenv, find_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler

load_dotenv(find_dotenv())

token = os.environ.get('BOT_ACCESS_TOKEN')
print(token)

updater = Updater(token=token)

dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Welcome to Kiltiskahvi bot. ")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
