import requests


def get_list(cube_id, api_endpoint='cubecobra.com', scheme='https'):
    # Calls the /cube/api/cubelist/ endpoint to get cards for a given cube ID.
    # Ex: https://cubecobra.com/cube/api/cubelist/cqz

    request_url = "{}://{}/cube/api/cubelist/{}".format(
        scheme, api_endpoint, cube_id)
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
