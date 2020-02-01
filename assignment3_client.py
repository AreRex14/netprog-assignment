# python 3

import socket

HOST = '127.0.0.1' 
PORT = 21115

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	# create a connection
	s.connect((HOST, PORT))

	msg = str(input("Sending: "))

	while msg != 'quit':
		if msg != 'ping':
			s.send(msg.encode('ascii'))
		else:
			msg = 'ping'
			s.send(msg.encode('ascii'))
		
		msg = s.recv(1024)
		print("Received: %s" % msg.decode('ascii'))
		msg = str(input("Sending: "))    
	s.send(msg.encode('ascii'))
	s.close()