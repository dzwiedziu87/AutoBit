import json
import urllib.request
import matplotlib.pyplot as plt
import itertools

request_ticker = urllib.request.urlopen('https://bitbay.net/API/Public/BTCPLN/ticker.json')
data_ticker = json.loads(request_ticker.read().decode('utf-8'))

request_order = request_ticker = urllib.request.urlopen('https://bitbay.net/API/Public/BTCPLN/orderbook.json')
data_order = json.loads(request_order.read().decode('utf-8'))

bids = data_order['bids']
asks = data_order['asks']

bid_x,bid_y = zip(*bids)
ask_x,ask_y = zip(*asks)

bid_y = list(itertools.accumulate(bid_y))
ask_y = list(itertools.accumulate(ask_y))

min_y = min(bid_y+ask_y)
max_y = max(bid_y+ask_y)

plt.plot(bid_x,bid_y,label='aids')
plt.plot(ask_x,ask_y,label='asks')
for key in 'max','min','last','vwap','average':
    plt.plot((data_ticker[key],data_ticker[key]),(min_y,max_y),linestyle=':',label=key+'='+str(data_ticker[key]))

plt.legend()
plt.show()