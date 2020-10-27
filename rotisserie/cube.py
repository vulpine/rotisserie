import cubecobra
from card import Card


class Cube:
    """
    A cube consists of a map of card names to individual Card objects.
    """

    def __init__(self):
        self.cube_map = {}

    def add_card(self, cardname):
        """
        Add a card name to this cube.
        """
        instance = Card(cardname)
        self.cube_map[cardname] = instance

    def import_cube(self, cube_id):
        """
        Get the full cube by ID from CubeCobra.
        Add each one to our map.
        """
        card_names = cubecobra.get_list(cube_id)

        for cardname in card_names:
            self.add_card(cardname)

    def get_cards(self):
        """
        Return the full cube list.
        """
        return self.cube_map
