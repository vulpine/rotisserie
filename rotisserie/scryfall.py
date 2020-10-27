import requests

# Get a card and its associated metadata from Scryfall.
class Scryfall:
    @staticmethod
    def cards_named(cardname, fuzzy=False, api_endpoint = 'api.scryfall.com', scheme = 'https'):
        # Calls the /cards/named endpoint to get metadata for a specific card.
        # https://scryfall.com/docs/api/cards/named
        parameter = "exact"
        if fuzzy:
            print("DEBUG: Fuzzy card handling enabled")
            parameter = "fuzzy"

        searchterm = '+'.join(cardname.lower().split(' '))
        querystring="{}={}".format(parameter,searchterm)
        request_url = "{}://{}/cards/named?{}".format(scheme, api_endpoint, querystring)
        print("DEBUG: requesting " + request_url)

        response = {}
        request = requests.get(request_url)
        if request.status_code == 200:
            response = request.json()
        else:
            print("DEBUG: got non-200 response {} for {}".format(request.status_code), request_url)
        return response

    @staticmethod
    def import_card(cardname):
        print ("DEBUG: processing {}".format(cardname))
        # Creates a Card object for the specified card name.
        card_data = Scryfall.cards_named(cardname)
        if card_data:
            if 'card_faces' in card_data.keys():
                print('DEBUG: {} is a double-faced card'.format(cardname))
                front_face = card_data['card_faces'][0]
                rear_face = card_data['card_faces'][1]
            else:
                # All data for a single-faced card is on the front face.
                front_face = card_data
            try:
                type_line = front_face['type_line']
                card_types = type_line.split('—')[0].rstrip().split(' ') # Careful! '—' is an em dash
                sub_types = type_line.split('—')[1].lstrip().split(' ')
                mana_cost = front_face['mana_cost']
                cmc = int(card_data['cmc'])  # A double-faced card's CMC is in the 'card_data', since it's a property of the entire card

                return card_types, sub_types, mana_cost, cmc
            except KeyError as e:
                print(e)
                print('Available keys for front face: {}'.format(front_face.keys()))
        return False