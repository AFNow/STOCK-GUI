import requests
from bs4 import BeautifulSoup
base_url = "https://www.google.com/finance"
company_index = "NASDAQ"
company_name = "NVDA" 
lang = "en"
end_url = f"{base_url}/quote/{company_name}:{company_index}?hl={lang}"
# Creating na HTTP request
page = requests.get(end_url)
# Grabbing content using parser
soup = BeautifulSoup(page.content, "html.parser")
# Description
cost_items = soup.find_all("div", {"class": "YMlKec fxKbKc"})
print (cost_items)
#print (cost_items)
last_close_items = soup.find_all('div', {'class': 'eYanAe'})
#print (last_close_items)
# Packing the description in dictionary by iterator
stock_description = {}
stock_description['item_cost'] = soup.find("div", {"class": "YMlKec fxKbKc"}).text[1:]
stock_description['last_close'] = soup.find("div", {"class": "P6K39c"}).text[1:]
stock_description['change'] =float(stock_description.get('item_cost')) - float(stock_description.get('last_close'))
print(stock_description)

# https://habr.com/ru/articles/544828/