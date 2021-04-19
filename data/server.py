#!/usr/bin/python3

import socket
import time
import sys

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', int(sys.argv[1])))
serv_sock.listen(10)

while True:

    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:

        data = client_sock.recv(1024)        
        if not data:
            break

        print(time.strftime('%T'),'Request:\n', data.decode('utf-8'))
    
        req_line = str(data, 'utf-8')
        words = req_line.split()
        
        if len(words) > 1 and words[0] == 'GET' and words[1] == '/ping':
            print('Received GET and /ping, sending pong...\n')
            client_sock.send('pong'.encode('utf-8'))

    client_sock.close()
