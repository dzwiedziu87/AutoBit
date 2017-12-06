import json
from datetime import datetime, timedelta
from pprint import pprint
from urllib.request import urlopen


class Api:
    __base_url = 'https://bitbay.net/API/Public/{currency}PLN/trades.json?sort=desc'
    __valid_currency = ("BTC", "ETH", "LSK", "LTC", "GAME", "DASH", "BCC")
    __data = []

    def __init__(self, currency, timeLimit):
        self.set_timelimit(timeLimit)
        self.set_currency(currency)

    def __str__(self):
        return "Api({currency},{time_limit})".format(currency=self.currency, time_limit=self.__time_limit)

    def set_currency(self, currency):
        if not currency in self.__valid_currency:
            raise ValueError('not valid currency')
        self.currency = currency

    def set_timelimit(self, timeLimit):
        if timeLimit[-1] == 'd':
            self.__time_limit = timedelta(days=int(timeLimit[:-1]))
        elif timeLimit[-1] == 'h':
            self.__time_limit = timedelta(hours=int(timeLimit[:-1]))
        elif timeLimit[-1] == 'm':
            self.__time_limit = timedelta(minutes=int(timeLimit[:-1]))
        else:
            raise ValueError('not valid timelimit')

    def __build_base_url(self):
        return self.__base_url.format(currency=self.currency)

    def build_url(self, since=''):
        if since:
            return self.__build_base_url() + '&since={since}'.format(since=since)
        else:
            return self.__build_base_url()

    def __download(self, url):
        response = urlopen(url)
        return json.loads(response.read().decode('utf-8'))

    def __limit(self):
        time = datetime.now() - self.__time_limit
        return time.timestamp()

    def __parse_since(self, data):
        return data[-1]['tid']

    def __parse_date(self, data):
        return data[-1]['date']

    def update(self):
        since = None
        self.__data = []
        limit = self.__limit()

        while True:
            current_data = self.__download(self.build_url(since))

            if not len(current_data):
                break

            self.__data += current_data

            last = self.__parse_date(self.__data)
            print(datetime.fromtimestamp(last))
            if last < limit:
                break

            since = self.__parse_since(self.__data)

    def data(self):
        return self.__data


api = Api("BTC", '1m')
print(api)
api.update()
pprint(api.data())
