from datetime import datetime

from bitbay import BitBayApi
import matplotlib.pyplot as plt

api = BitBayApi("BTC",'1h')
api.update()
print(api.data())

data_x = [x['date'] for x in api.data()]
data_y = [x['price'] for x in api.data()]

plt.plot(data_x,data_y)
plt.show()
