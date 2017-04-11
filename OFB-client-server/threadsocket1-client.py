#!/usr/bin/env python

"""
An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

import socket
import sys
from OFB import *

host = 'localhost'
port = 40035
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while 1:
    # read from keyboard
    print '>> ',
    data = sys.stdin.readline()

    if data== '\n':
        break
  
    data = OFB(data,'encrypt')
    print 'Decrypt : '+ data
    
    s.send(data)
    s.send('~~~')

    data = s.recv(size)
    
    real_data =''
    real_data += data

    while real_data[len(real_data)-3:len(real_data)]!='~~~':
        data = s.recv(size)
        real_data += data
        
    real_data = OFB(real_data[:len(real_data)-3],'decrypt')
    print 'server : ' + real_data.strip()
    
s.close()