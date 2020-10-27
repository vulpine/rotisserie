import cubecobra
from bot import Bot
from cube import Cube


if __name__ == "__main__":
    mycube = Cube()
    # This isn't a secret. Feel free to look at my cube. It's rad.
    mycube.import_cube('cqz')

    # Example: get Liliana's CMC
    print("LOTV's CMC is: {}".format(
        mycube.get_cards()['Liliana of the Veil'].cmc))

    # Set up our bot
    telegram = Bot(secretfile='/Users/smatthews/rotisserie/key.yaml')

    # and see if it can be interacted with?
    telegram.check_for_updates()
