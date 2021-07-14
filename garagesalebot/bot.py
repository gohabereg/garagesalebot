from os import getenv
from telegram.ext import Updater, MessageHandler, Filters, Dispatcher
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

class Bot: 
    def __init__(self):
        self.updater: Updater = Updater(token=getenv('BOT_TOKEN'))
        self.dispatcher: Dispatcher = self.updater.dispatcher
        
        self.dispatcher.add_handler(MessageHandler(Filters.text, self.echo))

        self.updater.start_polling()

        print('Bot started')

    def echo(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(update.message.text)

