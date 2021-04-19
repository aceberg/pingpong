#!/usr/bin/python3

import socket
from time import sleep
import time
import sys

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('pong_server', int(sys.argv[1])))
data = 'GET /ping HTTP/1.1\r\nHost: pong_server'

while True:
    print('\n' + time.strftime('%T'), ' Client request:', data)
    client_sock.send(data.encode('utf-8'))
    result = client_sock.recv(1024)
    print('Server responce:', result.decode('utf-8'))
    sleep(5)

client_sock.close()

