import requests
from bs4 import BeautifulSoup
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
    stock_description['last_close'] = soup.find("div", {"class": "P6K39c"}).text[1:]
    stock_description['change'] =float(stock_description.get('item_cost')) - float(stock_description.get('last_close'))
    return stock_description


    # Writing the stock_description to the file
def saving_stock(stock_name, index):
    print (stock_name, index)
    with open('stocks.json', mode = 'r+', encoding='utf-8') as file:
        text = file.read()
        if stock_name in text:
            print('text has ' + stock_name)
        else:
            file.write('{"stock_name": "' + stock_name + '", "company_index": "' + index + '"}' + '\n')


def index_selection():
    pass
