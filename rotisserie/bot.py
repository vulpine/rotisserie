import logging
import telegram
import yaml

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class Bot:
    """
    The Telegram bot, which handles fetching messages from Telegram, and sending
    replies back.
    """

    def __init__(self, secretfile="../key.yaml"):
        try:
            with open(secretfile, 'r') as f:
                yamldata = yaml.safe_load(f)
                self.name = yamldata['telegram']['name']
                self.key = yamldata['telegram']['key']
            print(self.key)
            self.tele = telegram.Bot(token=self.key)
            print(self.tele.get_me())
        except KeyError as e:
            print("KeyError: {} does not exist in {}".format(e, secretfile))
        except FileNotFoundError:
            print("FileNotFoundError: {} does not exist".format(secretfile))

    def check_for_updates(self):
        print(self.tele.get_updates())
