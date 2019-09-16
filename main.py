import requests, re, os
from bs4 import BeautifulSoup
import time

requests.adapters.DEFAULT_RETRIES = 1000
url = 'http://www.gwgold.com.hk/get_data/getprice.php'

def query_price():
    try:
        url_gold = requests.get(url)
        soup = BeautifulSoup(url_gold.text, 'html.parser')
        all_dict = (eval(str(soup)))
        gold_dict = all_dict.get('GOLD')
        gold_now = gold_dict.get('latest')
        gold_high = gold_dict.get('high')
        gold_low = gold_dict.get('low')
        gold_info = "{n}, H:{h}, L:{l}".format(
            n=gold_now,h=gold_high,l=gold_low)
        print (gold_info, '-', time.strftime("%S", time.localtime()))
    except Exception:
        print('retry later',time.strftime("%H:%M:%S", time.localtime()))
        time.sleep(5)
        query_price()


while True:
    query_price()
    time.sleep(2)
