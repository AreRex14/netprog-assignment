import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connection to hostname on the port
s.connect(("localhost", 9999))

#receive message
msg = s.recv(1024)

print(msg.decode('ASCII'))

#close connection
s.close()