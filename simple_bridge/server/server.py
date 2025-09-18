import socket

HOST = "0.0.0.0"  # listen on all network interfaces inside the container
PORT = 5000

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on port {PORT}...")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")

data = conn.recv(1024).decode()
print("Received from consumer:", data)

conn.sendall("Hello from producer!".encode())
print("Sent reply to consumer.")

conn.close()
server_socket.close()
