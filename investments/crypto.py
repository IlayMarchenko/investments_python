import requests
from bs4 import BeautifulSoup


def get_bitcoin_price():
    request_result = requests.get('https://www.coindesk.com/price/bitcoin')
    soup = BeautifulSoup(request_result.text, 'html.parser')
    value = soup.select('.price-large')
    price_str = value[0].text
    result_list = [price_str[i] for i in range(len(price_str)) if price_str[i] != '$' and price_str[i] != ',']
    price_str = ''
    for number in result_list:
        price_str += number
    result = float(price_str)
    return result
