import json

class Card:
    def __init__(self, cardname, cardtype, manacost, cmc):
        self.cardname = cardname
        self.cardtype = cardtype
        self.manacost = manacost
        self.cmc = cmc
        self.drafted = None
