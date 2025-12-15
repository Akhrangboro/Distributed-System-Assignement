import socket
import pickle
import numpy as np
import time

HOST = "127.0.0.1"
PORT = 5000
N = 500   # keep small

A = np.random.randint(0, 10, (N, N))
B = np.random.randint(0, 10, (N, N))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Connected to server")

start = time.time()

s.sendall(pickle.dumps((A, B)))
s.shutdown(socket.SHUT_WR)

data = b""
while True:
    packet = s.recv(4096)
    if not packet:
        break
    data += packet

C = pickle.loads(data)

end = time.time()
print("Result received")
print("Time taken:", round(end - start, 4), "seconds")

s.close()
