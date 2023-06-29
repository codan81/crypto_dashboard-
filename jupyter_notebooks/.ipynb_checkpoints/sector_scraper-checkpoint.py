
import requests
import pandas as pd

#Scrape by ticker and sector
def get_crypto_data(tickers):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/info"
    parameters = {
        "symbol": ",".join(tickers),
        "CMC_PRO_API_KEY": API_KEY
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    crypto_data = []
    for ticker, info in data['data'].items():
        crypto_data.append([ticker, info['tags'][0]])
    return crypto_data

tickers = ['CRO', 'ADA', 'BTC', 'ONE', 'VET', 'USDC', 'DOGE', 'AUDIO']
crypto_data = get_crypto_data(tickers)
screener_all = pd.DataFrame(crypto_data, columns=["ticker", "sector"])


#Scrape by ticker and price
def get_price(tickers):
    API_KEY = "API_KEY"  # Replace this with your API key
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={','.join(tickers)}&convert=USD&CMC_PRO_API_KEY={API_KEY}"

    response = requests.get(url)
    data = response.json()
    
    prices = []
    for ticker in tickers:
        price = data['data'][ticker]['quote']['USD']['price']
        prices.append(price)
    
    return prices

tickers = ['CRO', 'ADA', 'BTC', 'ONE', 'VET', 'USDC', 'DOGE', 'AUDIO']
prices = get_price(tickers)
screener = pd.DataFrame({'Ticker': tickers, 'Price': prices})
print(screener)
