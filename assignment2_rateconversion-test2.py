print("######Welcome to foreign exchange rate, currency conversion######")

amt = int(input("Enter an amount: "))

import requests
import json

def currencyExchange():
	source = input("Source currency: ")
	output = input("Output currency: ")
	
	params = {'base' : source}
	url = 'https://exchangeratesapi.io/api/latest?'
	response = requests.get(url, params=params)
	data = json.load(response.text)
	print(data)
	print(data.rates[output] * amt)
	
currencyExchange()