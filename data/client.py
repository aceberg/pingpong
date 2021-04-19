#!/usr/bin/python3

import socket
from time import sleep
import time
import sys

def pong_connect(port):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_sock.connect(('pong_server', port))
    except:
        print('Server is unreachable!')
    return(client_sock)

pong_port = int(sys.argv[1])
data = 'GET /ping HTTP/1.1\r\nHost: pong_server'
client_sock = pong_connect(pong_port)

while True:
    print('\n' + time.strftime('%T'), ' Client request:', data)
    try:
        client_sock.send(data.encode('utf-8'))
        result = client_sock.recv(1024)
        print('Server responce:', result.decode('utf-8'))
    except:
        client_sock = pong_connect(pong_port)
    
    sleep(5)

client_sock.close()

