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
s.connect((host, port))

s.send(str(ga).encode('utf-8')) # send pow(g, a, p) to the server
gb = int(s.recv(1024).decode('utf-8')) # and wait to receive pow(g, b, p)
k = pow(gb, a, p) # compute secret key, pow(g, ab, p), used for encryption
f = Fernet(base64.urlsafe_b64encode(k.to_bytes(32, byteorder='little')))

print('Secret key:', k)

while True:
    m = input('Enter message: ')
    s.send(f.encrypt(m.encode('utf-8'))) # send message
    r = s.recv(1024)
    message = f.decrypt(r).decode('utf-8') # decrypt received message
    print('Received:', message)
    