import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to the port 
serversocket.bind(("localhost", 9999))

# listen for client request
serversocket.listen()

while True:
	#establish a connection
	clientsocket,addr = serversocket.accept()
	print("Got a something from %s" % str(addr))
	#send message
	msg='Thank you for connecting'
	clientsocket.send(msg.encode('ascii'))
    #receive message
    msg = serversocket.recv(1024)
    msg = msg.decode('ASCII'))
    if msg == 'ping':
        msg = 'pong'
        clientsocket.send(msg.encode('ASCII'))
        print(msg)
    print('ping')
    if msg == 'quit':
        print('Server stop')
	    #close connection
	    clientsocket.close()