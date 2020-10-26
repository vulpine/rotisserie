from scryfall import Scryfall
from cubecobra import Cubecobra


if __name__ == "__main__":
    scryfall = Scryfall()
    cubecobra = Cubecobra()

    cube_id = 'cqz' # This isn't a secret. Feel free to look at my cube. It's rad.
    card_names = cubecobra.get_list(cube_id)
    imported_cube = {}

    # We probably don't want to do this on startup or it will take a long time!
    # But doing it right now to debug parsing cards, etc.
    for cardname in card_names[0:5]:
        instance = scryfall.import_card(cardname)
        imported_cube[cardname] = instance

print(imported_cube)