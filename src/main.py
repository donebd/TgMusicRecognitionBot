import os

from telegram.ext import *

from constants import TELEGRAM_API_KEY, TEMP_DIR
from handlers import handle_message, handle_voice, handle_audio


def main():
    print("Bot initializing...")
    updater = Updater(TELEGRAM_API_KEY, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", handle_message))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    updater.dispatcher.add_handler(MessageHandler(Filters.voice, handle_voice))
    updater.dispatcher.add_handler(MessageHandler(Filters.audio, handle_audio))
    updater.start_polling(1)

    temp_dir = os.path.join(os.path.dirname(__file__), '..', TEMP_DIR)
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    print("Bot initializing complete!")

    updater.idle()



main()
