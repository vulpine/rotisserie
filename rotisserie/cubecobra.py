import requests

# Get a cube list from Cube Cobra.
class Cubecobra:
    def __init__(self):
        # Configure the Cubecobra object to perform future API requests.
        self.api_endpoint = 'cubecobra.com'
        self.scheme = 'https'

    def get_list(self, cube_id):
        # Calls the /cube/api/cubelist/ endpoint to get cards for a given cube ID.
        # Ex: https://cubecobra.com/cube/api/cubelist/cqz

        request_url = "{}://{}/cube/api/cubelist/{}".format(self.scheme, self.api_endpoint, cube_id)
        print("DEBUG: requesting " + request_url)

        response = []
        request = requests.get(request_url)
        if request.status_code == 200:
            print("200 OK from Cube Cobra")
            response = request.text.splitlines()
            print("DEBUG: Got {} cards".format(len(response)))
        else:
            print("DEBUG: got non-200 response {}".format(request.status_code))
        return response