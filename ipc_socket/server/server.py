import socket
import os
import time

SOCKET_PATH = "/sockets/ipc_socket.sock"

# Remove old socket file if exists
if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(SOCKET_PATH)
server.listen(1)

print({time.time()}, "Waiting for connection...")

conn, _ = server.accept()
print({time.time()}, "Client connected")

data = conn.recv(1024).decode()
print({time.time()}, "Received:", data)

conn.sendall(b"Hello from Server!")
print({time.time()}, "Sent reply")

conn.close()
server.close()

time.sleep(2) # Keep container alive for a bit (optional)
