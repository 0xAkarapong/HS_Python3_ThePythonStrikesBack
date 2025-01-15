import socket

HOST = '127.0.0.1'
PORT = 443
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Connecting to server...")
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))