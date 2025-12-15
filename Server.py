import socket
import pickle
import numpy as np

HOST = "127.0.0.1"
PORT = 5000

print("Server started")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Waiting for client...")
conn, addr = s.accept()
print("Client connected:", addr)

# Receive data in chunks
data = b""
while True:
    packet = conn.recv(4096)
    if not packet:
        break
    data += packet

A, B = pickle.loads(data)
print("Matrices received")

# Matrix multiplication
C = A @ B

# Send result back
conn.sendall(pickle.dumps(C))
print("Result sent")

conn.close()
s.close()
