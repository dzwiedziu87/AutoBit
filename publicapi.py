import json
import urllib.request

url = 'https://bitbay.net/API/Public/BTCPLN/all.json'


def download(url):
    return urllib.request.urlopen(url)


def decode(data):
    return json.loads(data.read().decode('utf-8'))


if __name__ == '__main__':
    print(decode(download(url)))
