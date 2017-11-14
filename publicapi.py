import json
import urllib.request

urls = {
    'ticker':'https://bitbay.net/API/Public/BTCPLN/ticker.json',
    'market':'https://bitbay.net/API/Public/BTCPLN/market.json',
    'order':'https://bitbay.net/API/Public/BTCPLN/orderbook.json',
    'trade':'https://bitbay.net/API/Public/BTCPLN/trades.json'
}

def download(url):
    """download data from url"""
    return urllib.request.urlopen(url)


def decode(data):
    """decode json"""
    return json.loads(data.read().decode('utf-8'))


if __name__ == '__main__':
    for k, v in urls.items():
        data = decode(download(v))
        print(data)
