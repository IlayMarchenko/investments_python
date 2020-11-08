import requests
from bs4 import BeautifulSoup


class Shares:
    @classmethod
    def get_aapl_shares_price(cls):
        request_result = requests.get('https://www.marketwatch.com/investing/stock/aapl')
        soup = BeautifulSoup(request_result.text, 'html.parser')
        for value in soup.select('.value'):
            if '%' not in value.text:
                return round(float(value.text), 2)

    @classmethod
    def get_fb_shares_price(cls):
        request_result = requests.get('https://www.marketwatch.com/investing/stock/fb')
        soup = BeautifulSoup(request_result.text, 'html.parser')
        for value in soup.select('.value'):
            if '%' not in value.text:
                return round(float(value.text), 2)

    @classmethod
    def get_ba_shares_price(cls):
        request_result = requests.get('https://www.marketwatch.com/investing/stock/ba')
        soup = BeautifulSoup(request_result.text, 'html.parser')
        for value in soup.select('.value'):
            if '%' not in value.text:
                return round(float(value.text), 2)
