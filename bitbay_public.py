from download import download

crypto_list = ['BTC', 'ETH', 'LSK', 'LTC', 'GAME', 'DASH', 'BCC', 'BTG']
type_list = ['trades', 'orderbook', 'market', 'ticker', 'all']

url = 'https://bitbay.net/API/Public/{crypto}PLN/{type}.json'


def api(crypto, type, since=None):
    current_url = url.format(crypto=crypto, type=type)
    if since:
        current_url = current_url + f'?since={since}'
    return download(current_url)
