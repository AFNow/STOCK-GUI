'''
This file contains side non-class functions

'''
import requests
from bs4 import BeautifulSoup
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
stocks_path = os.path.join(BASE_DIR, 'stocks.json')

def get_stock_data(stock_name, index):
    base_url = "https://www.google.com/finance"
    company_index = index
    company_name = stock_name
    lang = "en"
    end_url = f"{base_url}/quote/{company_name}:{company_index}?hl={lang}"
    # Creating an HTTP request
    page = requests.get(end_url)
    # Grabbing content using parser
    soup = BeautifulSoup(page.content, "html.parser")
    # Packing the description in dictionary
    stock_description = {}
    stock_description['item_cost'] = soup.find("div", {"class": "YMlKec fxKbKc"}).text[1:]
    if len(stock_description['item_cost']) >= 7:
        replace = stock_description['item_cost']
        replace = replace.replace(',', '')
        stock_description['item_cost'] = replace
    stock_description['last_close'] = soup.find("div", {"class": "P6K39c"}).text[1:]
    if len(stock_description['last_close']) >= 7:
        replace = stock_description['last_close']
        replace = replace.replace(',', '')
        stock_description['last_close'] = replace
    stock_description['change'] = float(stock_description.get('item_cost')) - float(stock_description.get('last_close'))
    print(stock_description)
    return stock_description


# Writing the stock_description to the file
def save_stock(stock_name, index):
    with open(stocks_path, mode = 'r+', encoding='utf-8') as file: # stocks.json
        text = file.read()
        if stock_name in text:
            pass
        else:
            file.write(stock_name +' '+ index + '\n')
