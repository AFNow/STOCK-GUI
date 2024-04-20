import pandas

import requests
from requests import ConnectionError

import datetime

from bs4 import BeautifulSoup

def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class': class_path})
    try:
        spans = web_content_div[0].find_all('span')
        texts = [span.get_text() for span in spans]
    except IndexError:
        texts = []
    return texts

def real_time_price(stock_id):
    url = 'https://www.google.com/finance/quote/' + stock_id + ':NASDAQ?hl=ru'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = web_content_div(web_content, 'enJeMd')
        if texts != []:
            price, change, a = texts[0], texts[1]
        else:
            price, change = [], []
        return price, change
    except ConnectionError:
        price, change = [], []
    return price, change

stock = ['NVDA']
print (real_time_price('NVDA'))