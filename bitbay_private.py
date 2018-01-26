import hashlib
import hmac
import time
from urllib.parse import urlencode

from send import send_request

__url = 'https://bitbay.net/API/Trading/tradingApi.php'


def __send(data):
    key_pub = __read_from_file('key_pub')
    key_priv = __read_from_file('key_priv')

    data['moment'] = int(time.time())
    data_encoded = urlencode(data).encode()
    data_signed = hmac.new(key_priv.encode(), data_encoded, hashlib.sha512).hexdigest()

    header = {
        'API-Key': key_pub,
        'API-Hash': data_signed
    }

    response_decoded = send_request(__url, data_encoded, header)

    return response_decoded


def info():
    return __send({
        'method': 'info'
    })


def trade(type, currency, payment_currency, amount, price):
    return __send({
        'method': 'trade',
        'type': type,
        'currency': currency,
        'payment_currency': payment_currency,
        'amount': amount,
        'rate': price
    })


def cancel(id):
    return __send({
        'method': 'cancel',
        'id': id
    })


def orderbook(order_currency, payment_currency):
    return __send({
        'method': 'orderbook',
        'order_currency': order_currency,
        'payment_currency': payment_currency
    })


def orders():
    return __send({
        'method': 'orders'
    })


def history(currency):
    return __send({
        'method': 'history',
        'currency': currency
    })


def transactions():
    return __send({
        'method': 'transactions'
    })


def __read_from_file(file_name):
    with open(file_name) as file:
        return file.readline().strip()
