#!/usr/bin/env python3

import cubecobra
from telegram import Telegram
from card import Card



if __name__ == "__main__":
    # This isn't a secret. Feel free to look at my cube. It's rad.
    cube_id = 'cqz'
    card_names = cubecobra.get_list(cube_id)
    imported_cube = {}

    # Instantiate Card objects for every card name. By default, they have no details.
    for cardname in card_names:
        instance = Card(cardname)
        imported_cube[cardname] = instance
    
    telegram = Telegram()


#print(imported_cube)
#print(imported_cube['Liliana of the Veil'].cmc)
#print(imported_cube['Liliana of the Veil'].subtypes)
#print(imported_cube['Liliana of the Veil'].cardtypes)
#print(imported_cube['Liliana of the Veil'].manacost)
