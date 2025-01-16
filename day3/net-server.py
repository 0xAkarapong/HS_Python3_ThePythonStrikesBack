import socket
import threading

HOST = '0.0.0.0'
PORT = 21002
clients = []

def broadcast_message(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error sending message to client: {e}")
                client.close()
                clients.remove(client)

def handle_client(conn, addr):
    print('Connection accepted from ', addr)
    clients.append(conn)

    with conn:
        while True:
            message_received = ""
            while True:
                data = conn.recv(32)
                if data:
                    print('Received data chunk from client: ', repr(data))
                    message_received += data.decode()
                    if message_received.endswith("\n"):
                        break
                else:
                    print("Connection lost!")
                    break

            if message_received:
                print("Received message: ", message_received)
                broadcast_message(message_received.encode(), conn)
            else:
                break

    print(f"Connection with {addr} closed")
    clients.remove(conn)
    conn.close()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except OSError as msg:
    s = None
    print(f"Error creating socket: {msg}")
    exit(1)

try:
    s.bind((HOST, PORT))
    s.listen()
    print("Socket bound and listening")
except OSError as msg:
    print("Error binding/listening!")
    s.close()
    exit(1)

while True:
    conn, addr = s.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()

s.close()
print("Server finished")