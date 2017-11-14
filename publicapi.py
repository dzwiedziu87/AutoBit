import json
import urllib.request

ticker_url = 'https://bitbay.net/API/Public/BTCPLN/ticker.json'
market_url = 'https://bitbay.net/API/Public/BTCPLN/market.json'
orderbook_url = 'https://bitbay.net/API/Public/BTCPLN/orderbook.json'
trades_url = 'https://bitbay.net/API/Public/BTCPLN/trades.json'


def download(url):
    """download data from url"""
    return urllib.request.urlopen(url)


def decode(data):
    """decode json"""
    return json.loads(data.read().decode('utf-8'))


if __name__ == '__main__':
    print(decode(download(ticker_url)))
    print(decode(download(market_url)))
    print(decode(download(orderbook_url)))
    print(decode(download(trades_url)))
