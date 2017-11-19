import json
import urllib.request

_url_ticker = 'https://bitbay.net/API/Public/BTCPLN/ticker.json'
_url_order = 'https://bitbay.net/API/Public/BTCPLN/orderbook.json'

def _request(url):
    """return request object"""
    return urllib.request.urlopen(url)

def _data(request):
    """return dict with data parsed from json from request object"""
    return json.loads(request.read().decode('utf-8'))

def data_ticker():
    return _data(_request(_url_ticker))

def data_order():
    return _data(_request(_url_order))