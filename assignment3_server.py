# python 3

import socket

HOST = '127.0.0.1' 
PORT = 21115

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
	# bind to the port
	serversocket.bind((HOST, PORT))
	# listening for connection
	serversocket.listen()
	# add code for server timeout if those not receive any connection within 20000ms
	# establish a connection
	conn, addr = serversocket.accept()

msg = "pong"

while True:
	#print("Got a connection from %s" % str(addr))
	data = conn.recv(1024)
	if data.decode('ascii') == 'ping':
		print("Received: %s" % data.decode('ascii'))
		msg = "pong"
		print("Sending: %s" % msg)
		conn.send(msg.encode('ascii'))
	elif data.decode('ascii') == 'quit':
		msg = 'quit'
		conn.send(msg.encode('ascii'))
		print("Server stop")
		# close connection
		conn.close()
		# terminate the process
		exit()
	else:
		# drop other invalid message to server
		# send invalid to client, until the right message is send, that is ping
		msg = 'Invalid'
		conn.send(msg.encode('ascii'))
conn.close()