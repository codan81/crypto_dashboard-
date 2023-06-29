

import requests
import pandas as pd
import json

API_KEY = "YOUR_API_KEY"
def get_crypto_data(tickers):
    url = f"https://rest.coinapi.io/v1/assets?filter_asset_id={','.join(tickers)}"
    headers = {'X-CoinAPI-Key' : 'YOUR_API_KEY_HERE'}
    response = requests.get(url, headers=headers)
    data = response.content.decode('utf-8')
    data = json.loads(data)

    crypto_data = []
    for asset in data:
        crypto_data.append([asset['asset_id'], asset['type_is_crypto']])
    return crypto_data

# Scrape by ticker and sector
# def get_crypto_data(tickers):
#     url = f"https://rest.coinapi.io/v1/assets?filter_asset_id={','.join(tickers)}"
#     headers = {'X-CoinAPI-Key' : 'YOUR_API_KEY_HERE'}
#     response = requests.get(url, headers=headers)
#     data = json.loads(response.content.decode('utf-8'))

#     crypto_data = []
#     for asset in data:
#         crypto_data.append([asset['asset_id'], asset['type_is_crypto']])
#     return crypto_data


# def get_crypto_data(tickers):
#     url = "https://api.coinapi.io/v1/assets"
#     parameters = {
#         "filter_asset_id": ",".join(tickers),
#         "apikey": API_KEY
#     }
#     response = requests.get(url, params=parameters)
#     data = response.json()
#     crypto_data = []
#     for asset in data:
#         crypto_data.append([asset['asset_id'], asset['type_is_crypto']])
#     return crypto_data

# Get the price for a given ticker
def get_price(ticker):
    url = f"https://api.coinapi.io/v1/ohlcv/{ticker}/USD/history"
    params = {
        "period_id": "1DAY",
        "time_start": "2010-01-01T00:00:00",
        "apikey": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    price = data[-1]['price_close']
    return price

# Get the prices for a list of tickers
def get_prices(tickers):
    prices = []
    for ticker in tickers:
        price = get_price(ticker)
        prices.append(price)
    return prices

tickers = ['CRO', 'ADA', 'BTC', 'ONE', 'VET', 'USDC', 'DOGE', 'AUDIO']
crypto_data = get_crypto_data(tickers)
screener_all = pd.DataFrame(crypto_data, columns=["Ticker", "Is Crypto"])
prices = get_prices(tickers)
screener = pd.DataFrame({'Ticker': tickers, 'Adj Close Price': prices})
print(screener)
