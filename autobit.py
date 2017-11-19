from api import data_order,data_ticker
import matplotlib.pyplot as plt
import itertools

data_ticker = data_ticker()
data_order = data_order()

bids = data_order['bids']
asks = data_order['asks']

bid_x,bid_y = zip(*bids)
ask_x,ask_y = zip(*asks)

bid_y = list(itertools.accumulate(bid_y))
ask_y = list(itertools.accumulate(ask_y))

plt.plot(bid_x,bid_y,label='aids')
plt.plot(ask_x,ask_y,label='asks')
for key in 'max','min','last','vwap','average':
    plt.axvline(data_ticker[key],linestyle=':',label=key+'='+str(data_ticker[key]))

plt.legend()
plt.show()