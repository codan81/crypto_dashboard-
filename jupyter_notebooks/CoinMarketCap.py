#Imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from glob import glob
import json
import time
from cryptocmd import CmcScraper

# # Simple get request of the main page into the BeautifulSoup object.
# cmc = requests.get('https://coinmarketcap.com/')
# soup = BeautifulSoup(cmc.content, 'html.parser')
    
# """
#     This will give us the entire web page, and we can specify different parts of the page like     this:

#     """

# # print(soup.title)

# """
#     JSON data within a script tag so we’ll need to isolate it.
    
#     """

# data = soup.find('script', id="__NEXT_DATA__", type = 'application/json')

# coins = {}

# # using data.contents[0] to remove scrip tags
# coin_data = json.loads(data.contents[0])
# listings = coin data  

# initialise scraper without time interval
scraper = CmcScraper('VET')

# get raw data as list of list
headers, data = scraper.get_data()

# get data in a json format
vet_json_data = scraper.get_data("json")

# export the data as csv file, you can also pass optional `name` parameter
scraper.export("csv", name="VET_all_time")

# Pandas dataFrame for the same data
df = scraper.get_dataframe()
print(df)


#scrape price and sector from coin market cap
import requests
from bs4 import BeautifulSoup

def get_cmc_data(ticker):
    url = f"https://coinmarketcap.com/currencies/{ticker}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find("span", class_="cmc-details-panel-price__price").get_text().strip()
    sector = soup.find("div", class_="cmc-details-panel-sector").get_text().strip()
    return {"ticker": ticker, "price": price, "sector": sector}

tickers = ["bitcoin", "ethereum", "litecoin"]
data = [get_cmc_data(ticker) for ticker in tickers]
print(data)
