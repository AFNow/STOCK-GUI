import requests
from bs4 import BeautifulSoup
import json
def get_stock_data(stock_name):
    base_url = "https://www.google.com/finance"
    company_index = "NASDAQ"
    company_name = stock_name
    lang = "en"
    end_url = f"{base_url}/quote/{company_name}:{company_index}?hl={lang}"
    # Creating na HTTP request
    page = requests.get(end_url)
    # Grabbing content using parser
    soup = BeautifulSoup(page.content, "html.parser")
    # Packing the description in dictionary
    stock_description = {}
    stock_description['item_cost'] = soup.find("div", {"class": "YMlKec fxKbKc"}).text[1:]
    stock_description['last_close'] = soup.find("div", {"class": "P6K39c"}).text[1:]
    stock_description['change'] =float(stock_description.get('item_cost')) - float(stock_description.get('last_close'))
    
    # Writing the stock_description to the file
#    with open('stocks.json', mode = 'r+', encoding='utf-8') as file:
#        text=json.load()
#        if stock_name in text:
#            print('text has ' + stock_name)
#        else:
#            file.write('{"stock_name": "' + stock_name + '", "company_index": "' + company_index + '"}' + '\n')
#   return stock_description


#def update_stock(stock_name):
#    base_url = "https://www.google.com/finance"
#    company_index = "NASDAQ"
#    company_name = stock_name
#    lang = "en"
#    end_url = f"{base_url}/quote/{company_name}:{company_index}?hl={lang}"
#    page = requests.get(end_url)
#    soup = BeautifulSoup(page.content, "html.parser")
#    stock_description = {}
#    while True:
#        stock_description['item_cost'] = soup.find("div", {"class": "YMlKec fxKbKc"}).text[1:]
#        stock_description['last_close'] = soup.find("div", {"class": "P6K39c"}).text[1:]
#        stock_description['change'] =float(stock_description.get('item_cost')) - float(stock_description.get('last_close'))
#        return stock_description
