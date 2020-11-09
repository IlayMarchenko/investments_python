from db.init_database import init_database
from db.add_to_db import add_to_db
from currency import Currency
from gold import get_gold_price
from shares import Shares
from crypto import get_bitcoin_price
import time
import datetime


if __name__ == '__main__':
    init_database('db/database.db')
    unix_time_now = int(time.time())

    add_to_db('aapl', unix_time_now, Shares.get_aapl_shares_price())
    add_to_db('ba', unix_time_now, Shares.get_ba_shares_price())
    add_to_db('btc', unix_time_now, get_bitcoin_price())
    add_to_db('eur', unix_time_now, Currency.get_eur_rate())
    add_to_db('fb', unix_time_now, Shares.get_fb_shares_price())
    add_to_db('gold', unix_time_now, get_gold_price())
    add_to_db('usd', unix_time_now, Currency.get_usd_rate())

    # print(unix_time)
    # print(datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S'))


