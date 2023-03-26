import socket

# Address
#HOST = '127.0.0.1'
HOST = '127.0.0.1'
PORT = 8001

request = 'can you hear me?'

# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

s.sendall(request.encode(encoding = "utf-8"))
reply = s.recv(100)
print('reply is:', reply)

if reply == b"Bye":
	print('Bye!')
	s.close()
