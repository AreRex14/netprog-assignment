print("######Welcome to foreign exchange rate, currency conversion######")

amt = int(input("Enter amount: "))

import requests

def currencyExchange():
	source = input("Source currency: ")
	output = input("Output currency: ")
	
	params = {'base' : source}
	url = 'https://exchangeratesapi.io/api/latest?'
	response = requests.get(url, params=params).json()
	
	print('Total money after conversion = ' , output ,' %d' % response['rates'][output] * amt)
	
currencyExchange()