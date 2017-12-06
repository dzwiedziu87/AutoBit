from bitbay import BitBayApi

api = BitBayApi("BTC",'1m')
api.update()
print(api.data())