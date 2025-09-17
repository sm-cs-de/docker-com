import socket
import time

HOST = "server"  # service name from docker-compose.yml
PORT = 5000

# wait a bit for the server to start
time.sleep(2)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = "Hello from client!"
client_socket.sendall(message.encode())
print("Sent to server:", message)

reply = client_socket.recv(1024).decode()
print("Received from server:", reply)

client_socket.close()
