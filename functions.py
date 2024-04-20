from yahoo_fin import stock_info
import time

def get_stock_data(stock_name):
    def get_cost(stock_name):
        stock_cost = float(stock_info.get_live_price(stock_name))
        return stock_cost
    return get_cost(stock_name)