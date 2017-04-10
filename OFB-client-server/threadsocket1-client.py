#!/usr/bin/env python

"""
An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

import socket
import sys
from OFB import *

host = 'localhost'
port = 50015
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while 1:
    # read from keyboard
    print '>> ',
    data = sys.stdin.readline()
    
    if data== '\n':
        break
    
    data = str(len(data))+", "+ data    
    data = OFB(data,'encrypt')
    print 'Decrypt : '+ data
    
    s.send(data)
    data = s.recv(size)
    
    data = OFB(data,'decrypt')
    temp_data2 = int(data.split(',')[0])
    
    looping=len(data.split(', ')[1])
    real_data =data.split(', ')[1]             
    
    while looping<temp_data2:
        data = s.recv(buff)                    
        looping=looping+len(data)
        real_data += data.strip()
        
    print 'server : ' + real_data.strip()
    
s.close()