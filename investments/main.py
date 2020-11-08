from db.init_database import init_database
from currency import Currency
from gold import get_gold_price
from shares import Shares
from crypto import get_bitcoin_price
import time
import datetime


if __name__ == '__main__':
    init_database('db/database.db')
    # print(Currency.get_eur_rate())
    # print(Currency.get_usd_rate())
    # print(Shares.get_aapl_shares_price())
    # print(Shares.get_fb_shares_price())
    # print(Shares.get_ba_shares_price())
    # print(get_gold_price())
    # print(get_bitcoin_price())
    # unix_time = int(time.time())
    # print(datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S'))
