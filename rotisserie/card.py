import json
from scryfall import Scryfall

class Card:
    def __init__(self, cardname):
        self.cardname = cardname
        self._cardtypes = None
        self._subtypes = None
        self._manacost = None
        self._cmc = None
        self.drafted_by = None         # Which player has drafted this card?


    """
    For each of the properties, if any one is unset, we call fetch_details() to set all of them
    to avoid unnecessary future calls to Scryfall.
    For example, if cmc is None, we set it, as well as mana cost, card types, etc.
    """
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
        self.cardtypes, self.subtypes, self.manacost, self.cmc = Scryfall.import_card(self.cardname)