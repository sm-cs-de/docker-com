import socket
import time

SOCKET_PATH = "/sockets/ipc_socket.sock"

# Wait a bit for the server to create the socket
time.sleep(1)

client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client.connect(SOCKET_PATH)

msg = "Hello from Client!"
client.sendall(msg.encode())
print({time.time()}, "Sent:", msg)

reply = client.recv(1024).decode()
print({time.time()}, "Received:", reply)

client.close()
