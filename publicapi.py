import json
import urllib.request
import matplotlib.pyplot as plt

urls = {
    'ticker' : 'https://bitbay.net/API/Public/BTCPLN/ticker.json',
    'order' : 'https://bitbay.net/API/Public/BTCPLN/orderbook.json',
}

def request(url):
    """download data from url"""
    return urllib.request.urlopen(url)


def decode(data):
    """decode json"""
    return json.loads(data.read().decode('utf-8'))

def valid(data):
    if 'code' in data:
        return False
    else:
        return True
        
def running_sum(data):
    total = 0
    for item in data:
        total += item
        yield total

if __name__ == '__main__':

    data_ticker = decode(request(urls.get('ticker')))
    print('ticker', data_ticker)

    data_order = decode(request(urls.get('order')))
    if not valid(data_order):
        print('error')

    bids = data_order.get('bids')
    asks = data_order.get('asks')
    print('order bids',len(bids),bids)
    print('order asks', len(asks), asks)

    bid_x,bid_y = zip(*data_order.get('bids'))
    ask_x,ask_y = zip(*data_order.get('asks'))

    bid_y = list(running_sum(reversed(bid_y)))
    ask_y = list(running_sum(ask_y))

    min_y = min(bid_y+ask_y)
    max_y = max(bid_y+ask_y)

    plt.plot(bid_x,bid_y,label='aids')
    plt.plot(ask_x,ask_y,label='asks')
    for key in 'max','min','last','vwap','average':
        plt.plot((data_ticker[key],data_ticker[key]),(min_y,max_y),linestyle=':',label=key+'='+str(data_ticker[key]))

    plt.legend()
    plt.show()




