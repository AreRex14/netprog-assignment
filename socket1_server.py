import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to the port 
serversocket.bind(("localhost", 9999))

#queue up to 5 requests
serversocket.listen(5)

while True:
	#establish a connection
	clientsocket,addr = serversocket.accept()
	print("Got a something from %s" % str(addr))
	#send message
	msg='Thank you for connecting'
	clientsocket.send(msg.encode('ascii'))
	#close connection
	clientsocket.close()