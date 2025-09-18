import socket
import time

HOST = "producer"  # service name from docker-compose.yml
PORT = 5000

# wait a bit for the producer to start
time.sleep(2)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = "Hello from consumer!"
client_socket.sendall(message.encode())
print("Sent to producer:", message)

reply = client_socket.recv(1024).decode()
print("Received from producer:", reply)

client_socket.close()
