import requests
#import json 

print("######Welcome to foreign exchange rate, currency conversion######")
print("The base rate is by default is Euro.")

#Below statements only to demonstrate when to use import json, it is used only for
#accessing json to present it in more readable way 
#you can remove the import json comment and comments below and see it in action
#url = 'https://exchangeratesapi.io/api/latest'
#response = requests.get(url)
#data = json.dumps(json.loads(response.text), indent=4)
#print(data)
#

#Statements below will executed good without importing json 
amt = int(input("Enter amount: "))

while amt != 0:
	
	src = input("Source currency: ")
	out = input("Output currency: ")
	#To convert to uppercase
	src = src.upper()
	out = out.upper()
	
	def currencyExchange():
		#Take base rate as parameter
		params = {'base' : src}
		url = 'https://exchangeratesapi.io/api/latest?'
		#This will append to the url as request parameter
		response = requests.get(url, params=params).json()
		#just need to access the field required and add the out parameter as one of the json field, out value is string so no problem
		result = str(response['rates'][out] * amt)
		print('Total money after conversion = ',out,' ',result)


	currencyExchange()
	print('Thank you for using this service. Insert 0 to exit')
	amt = int(input("Enter another amount: "))
print("Thank you for using the service.")