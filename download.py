import json
from urllib.request import urlopen


def download(url):
    response = urlopen(url)
    data = response.read().decode()
    data_decoded = json.loads(data)
    return data_decoded
