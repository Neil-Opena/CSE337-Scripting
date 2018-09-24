#One Step Ahead


from bs4 import BeautifulSoup
import urllib.request

def is_a_data_row(css_class):
    return "data-row" in css_class

def get_symbol(data_row):
    temp = data_row.find("a", "Fw(b)")
    return temp.text

def get_name(data_row):
    temp = data_row.find("td","data-col1 Ta(start) Pend(10px)")
    return temp.text

def get_last_price(data_row):
    temp = data_row.find("td","data-col2 Ta(end) Pstart(20px)")
    return temp.text

def get_market_time(data_row):
    temp = data_row.find("td","data-col3 Ta(end) Pstart(20px)")
    return temp.text

def get_change(data_row):
    temp = data_row.find("td","data-col4 Ta(end) Pstart(20px)")
    return temp.text

output_file = open("commodities.txt", "w")
url_response = urllib.request.urlopen("https://finance.yahoo.com/commodities")

commodities_soup = BeautifulSoup(url_response, 'html.parser')

commodities_data = commodities_soup.find_all("tr",class_=is_a_data_row)

for data_row in commodities_data:
    #get the symbol
    symbol = get_symbol(data_row)
    #get the name
    name = get_name(data_row)
    #get the last price
    last_price = get_last_price(data_row)
    #get the market time
    market_time = get_market_time(data_row)
    #get the change
    change = get_change(data_row)
    print(change)




output_file.close()
