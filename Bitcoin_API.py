import requests

def price():
	response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=usd')
	price = float(response.json()['data']['amount'])
	return price

print(price())
