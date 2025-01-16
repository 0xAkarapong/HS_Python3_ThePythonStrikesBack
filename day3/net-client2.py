import socket
import threading

HOST = '127.0.0.1'
PORT = 21002


def send_message_function(client_socket):
    while True:
        message = input("Enter a message: ")
        client_socket.send((message + "\n").encode())


def receive_message_function(client_socket):
    while True:
        message_received = ""
        while True:
            data = client_socket.recv(32)
            if data:
                message_received += data.decode()
                if message_received.endswith("\n"):
                    print(f"Received message: {message_received}")
                    break
            else:
                print("Connection lost!")
                return


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    send_thread = threading.Thread(target=send_message_function, args=(s,))
    receive_thread = threading.Thread(target=receive_message_function, args=(s,))

    send_thread.start()
    receive_thread.start()

    send_thread.join()
    receive_thread.join()

print("Client finished")