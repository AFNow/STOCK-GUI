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
items = soup.find_all("div", {"class": "ln0Gqe"})
# Packing the description in dictionary by iterator
stock_description = {}
for item in items:
    stock_description['item_cost'] = item.find("div", {"class": "YMlKec fxKbKc"}).text
    #item_raise = item.find("jsname", {"class": "NydbP VOXKNe tnNmPe"}).text
print(stock_description)
#print(item_raise)

# https://habr.com/ru/articles/544828/