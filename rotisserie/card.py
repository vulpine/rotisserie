import json
import scryfall


class Card:
    """
    Stores details for a specific card in a cube.

    On instantiation, we provide just the card name, to avoid calling Scryfall repeatedly and
    taking a long time. When we first request any of the properties, we then call the Scryfall
    API, and set all of them.
    """

    def __init__(self, cardname):
        self.cardname = cardname
        self._cardtypes = None
        self._subtypes = None
        self._manacost = None
        self._cmc = None
        self.drafted_by = None         # TODO: Which player has drafted this card?

    @property
    def cmc(self):
        if self._cmc == None:
            self.fetch_details()
        return self._cmc

    @cmc.setter
    def cmc(self, value):
        self._cmc = value

    @property
    def cardtypes(self):
        if self._cardtypes == None:
            self.fetch_details()
        return self._cardtypes

    @cardtypes.setter
    def cardtypes(self, value):
        self._cardtypes = value

    @property
    def subtypes(self):
        if self._subtypes == None:
            self.fetch_details()
        return self._subtypes

    @subtypes.setter
    def subtypes(self, value):
        self._subtypes = value

    @property
    def manacost(self):
        if self._manacost == None:
            self.fetch_details()
        return self._manacost

    @manacost.setter
    def manacost(self, value):
        self._manacost = value

    def fetch_details(self):
        self.cardtypes, self.subtypes, self.manacost, self.cmc = scryfall.import_card(
            self.cardname)
