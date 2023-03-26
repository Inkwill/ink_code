import socket

# Address
HOST = '127.0.0.1'
PORT = 8001

reply = 'Yes'

# Configure socket
	# socket.socket()创建一个socket对象，并说明socket使用的是IPv4(AF_INET，IP version 4)和TCP协议(SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(3)
conn, addr = s.accept()
request = conn.recv(100)

print ('request is:', request)
print ('Connected by',addr)

conn.sendall(reply.encode(encoding = "utf-8"))
conn.close()

