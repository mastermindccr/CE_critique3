#!/usr/bin/python3

import socket
import random
import base64
from cryptography.fernet import Fernet

host = '172.18.0.3'
port = 12345

# Diffie-Hellman key exchange variables
p = 559010791577752610994053397793
g = 65537
a = random.randint(1, p-1)
ga = pow(g, a, p)

# socket configuration - server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

conn, addr = s.accept()

gb = int(conn.recv(1024).decode('utf-8')) # wait to receive pow(g, b, p)
k = pow(gb, a, p) # compute secret key, pow(g, ab, p), used for encryption
f = Fernet(base64.urlsafe_b64encode(k.to_bytes(32, byteorder='little')))
conn.send(str(ga).encode('utf-8')) # send pow(g, a, p) to the client

print('Secret key:', k)

while True:
    r = conn.recv(1024)
    message = f.decrypt(r).decode('utf-8')
    print('Received:', message)
    if message == 'ping':
        conn.send(f.encrypt('pong'.encode('utf-8')))
    elif message == 'hello':
        conn.send(f.encrypt('world'.encode('utf-8')))
    elif message == 'mitm':
        conn.send(f.encrypt('attack'.encode('utf-8')))
    else:
        conn.send(f.encrypt('qq'.encode('utf-8')))
    