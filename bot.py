import os
import picamera as pc
from dotenv import load_dotenv, find_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler

load_dotenv(find_dotenv())

camera = pc.PiCamera()

token = os.environ.get('BOT_ACCESS_TOKEN')
print(token)

updater = Updater(token=token)

dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Welcome to Kiltiskahvi bot. ")

def send_pic(bot, update):
    camera.capture('img.jpg') #todo: put this as file like object instead of writing
    bot.send_photo(chat_id=update.message.chat_id, photo=open('img.jpg', 'rb')) 
    bot.send_message(chat_id=update.message.chat_id, text="Welcome to Kiltiskahvi bot. ")
    os.remove('img.jpg')


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
send_pic_handler = CommandHandler('pic', send_pic)
dispatcher.add_handler(send_pic_handler)


updater.start_polling()
