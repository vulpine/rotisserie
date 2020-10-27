import yaml

class Telegram():
    def __init__(self, secretfile="../key.yaml"):
        with open(secretfile, 'r') as f:
            yamldata = yaml.safe_load(f)
        try:
            self.name = yamldata['telegram']['name']
            self.key = yamldata['telegram']['key']
        except KeyError as e:
            print(e)