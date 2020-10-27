import logging
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
import yaml

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class Bot:
    """
    The Telegram bot, which handles fetching messages from Telegram, and sending
    replies back.
    """

    def __init__(self, secretfile="../key.yaml"):
        self.started = False
        try:
            with open(secretfile, 'r') as f:
                yamldata = yaml.safe_load(f)
                self.name = yamldata['telegram']['name']
                self.token = yamldata['telegram']['token']
        except KeyError as e:
            print("{} does not exist in {}".format(e, secretfile))
            raise
        except FileNotFoundError:
            print("{} does not exist".format(secretfile))
            raise

        # Updater receives messages from telegram in a separate thread and delivers them
        # to a dispatcher
        # https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.updater.html#telegram.ext.updater.Updater
        self.updater = Updater(token=self.token)
        self.dispatcher = self.updater.dispatcher

        # Add handlers for various messages
        self.dispatcher.add_handler(
            CommandHandler('start', self.start_handler))
        self.dispatcher.add_handler(CommandHandler('stop', self.stop_handler))
        # Debug echo handler
        self.dispatcher.add_handler(MessageHandler(
            Filters.text & (~Filters.command), self.echo_handler))

    def start_handler(self, update, context):
        if not self.started:
            self.started = True
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Started.")
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="I've already started. Type '/stop' to finish.")

    def stop_handler(self, update, context):
        if self.started:
            self.started = False
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Stopped.")
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Can't stop what hasn't been started.")

    def echo_handler(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=update.message.text)

    def start_polling(self):
        self.updater.start_polling()
