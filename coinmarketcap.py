from download import download

id_valid_list = ['bitcoin','ethereum','bitcoin-cash','litecoin','dash','bitcoin-gold','lisk','gamecredits']

url = 'https://api.coinmarketcap.com/v1/ticker/{id}/?convert=PLN'

def ticker(id):
    return download(url.format(id=id))

