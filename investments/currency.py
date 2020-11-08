import requests


class Currency:
    @classmethod
    def get_usd_rate(cls):
        request_result = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json()
        dictionary = dict(request_result[0])
        return round(float(dictionary['buy']), 2)

    @classmethod
    def get_eur_rate(cls):
        request_result = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json()
        dictionary = dict(request_result[1])
        return round(float(dictionary['buy']), 2)
