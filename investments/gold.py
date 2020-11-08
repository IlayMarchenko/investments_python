import http.client
import json


def get_gold_price():
    conn = http.client.HTTPSConnection("www.goldapi.io")
    payload = ''
    headers = {
      'x-access-token': 'goldapi-19ve7pukh9ebtmj-io',
      'Content-Type': 'application/json'
    }
    conn.request("GET", "/api/XAU/USD", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    return round(float(data['price']), 2)
