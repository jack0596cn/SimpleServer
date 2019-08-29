#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:raytown
# time:2019/8/21

import socket

# Define an IP address and port as a tuple
ip_port = ('127.0.0.1',8888)

# Create an object and bind the IP address to start listening
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

# Start receiving messages
while True:
    print 'server waiting...'
    # Conn indicates the proprietary communication line after the client establishes a connection with the server.
    conn,addr = sk.accept() # Accept is blocked and will not continue to run without receiving a connection request

    # Receive messages from the client
    client_data = conn.recv(1024) # Recv is also blocked
    print client_data
    if client_data == 'loadPlayer|1':
        print("111111111111111")
    elif client_data == "AAA":
        conn.sendall("AAA_Resp")

    # close conn
    conn.close()