tempInt = int(input("Please enter a temperature: "))
while tempInt != 0:
	if tempInt >= 100:
		print("It is hot")
	
	elif tempInt <= 60:
		print("It is cold")
				
	else: 
		print("It is just right")
		
	tempInt = int(input("Please enter a temperature: "))
print("Good bye")