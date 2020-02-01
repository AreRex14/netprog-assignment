print("Welcome to foreign exchange rate, currency conversion")

amt = int(input("Enter an amount: "))

import requests

def currencyExchange():
	source = input("Base rate: ")
	output = input("Destination rate: ")
	
	url = 'https://exchangeratesapi.io/api/latest?base=USD'
	response = requests.get(url).json()
	
	print(response['rates'][output])

currencyExchange()