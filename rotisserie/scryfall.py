import requests

from card import Card

# Get a card and its associated metadata from Scryfall.
class Scryfall:
    def __init__(self):
        # Configure the Scryfall object to perform future API requests.
        self.api_endpoint = 'api.scryfall.com'
        self.scheme = 'https'

    def cards_named(self, cardname, fuzzy=False):
        # Calls the /cards/named endpoint to get metadata for a specific card.
        # https://scryfall.com/docs/api/cards/named
        parameter = "exact"
        if fuzzy:
            print("DEBUG: Fuzzy card handling enabled")
            parameter = "fuzzy"

        searchterm = '+'.join(cardname.lower().split(' '))
        querystring="{}={}".format(parameter,searchterm)
        request_url = "{}://{}/cards/named?{}".format(self.scheme, self.api_endpoint, querystring)
        print("DEBUG: requesting " + request_url)

        response = {}
        request = requests.get(request_url)
        if request.status_code == 200:
            response = request.json()
        else:
            print("DEBUG: got non-200 response {} for {}".format(request.status_code), request_url)
        return response

    def import_card(self, cardname):
        print ("DEBUG: processing {}".format(cardname))
        # Creates a Card object for the specified card name.
        card_data = self.cards_named(cardname)
        if card_data:
            if 'card_faces' in card_data.keys():
                print('DEBUG: {} is a double-faced card'.format(cardname))
                front_face = card_data['card_faces'][0]
                rear_face = card_data['card_faces'][1]
            else:
                # All data for a single-faced card is on the front face.
                front_face = card_data
            try:
                # A double-faced card's CMC is consistently that of its front face, so we look that 
                # up from from 'card_data', not from the front or rear face.
                card = Card(front_face['name'], front_face['type_line'], front_face['mana_cost'], card_data['cmc'])
                return card
            except KeyError as e:
                print(e)
                print('Available keys for front face: {}'.format(front_face.keys()))
        return False