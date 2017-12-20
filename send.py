import json
from urllib.request import Request, urlopen


def send_request(url, data_encoded, header):
    request = Request(url, data_encoded, header)
    response = urlopen(request)
    response_decoded = json.loads(response.read().decode())
    return response_decoded