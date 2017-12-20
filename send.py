import hashlib
import hmac
import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode

import time

url = 'https://bitbay.net/API/Trading/tradingApi.php'


def read_from_file(file_name):
    with open(file_name) as file:
        return file.readline()


key_pub = read_from_file('key_pub')
key_priv = read_from_file('key_priv')


def send(data):
    data['moment'] = int(time.time())
    data_encoded = urlencode(data).encode()
    data_signed = hmac.new(key_priv.encode(), data_encoded, hashlib.sha512).hexdigest()

    header = {
        'API-Key': key_pub,
        'API-Hash': data_signed
    }

    request = Request(url, data_encoded, header)
    response = urlopen(request)
    response_decoded = json.loads(response.read().decode())

    return response_decoded


def info():
    return send(
        {
            'method': 'info'
        }
    )


def trade(type, currency, payment_currency, amount, price):
    return send(
        {
            'method': 'trade',
            'type': type,
            'currency': currency,
            'payment_currency': payment_currency,
            'amount': amount,
            'rate': price
        }
    )


def cancel(id):
    return send(
        {
            'method': 'cancel',
            'id': id
        }
    )


def orderbook(order_currency, payment_currency):
    return send(
        {
            'method': 'orderbook',
            'order_currency': order_currency,
            'payment_currency': payment_currency
        }
    )


def orders():
    return send(
        {
            'method': 'orders'
        }
    )


def history(currency):
    return send(
        {
            'method': 'history',
            'currency': currency
        }
    )


def transactions():
    return send(
        {
            'method': 'transactions'
        }
    )
