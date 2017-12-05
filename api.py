import json
import urllib.request


def createUrl(currency_from, currency_to, category):
    """
    returns formatted url

    >>> createUrl('BTC','PLN','trades')
    'https://bitbay.net/API/Public/BTCPLN/trades.json'
    """
    return 'https://bitbay.net/API/Public/{currency_from}{currency_to}/{category}.json'.format(
        currency_from=currency_from, currency_to=currency_to, category=category)

if __name__ == "__main__":
    import doctest
    doctest.testmod()