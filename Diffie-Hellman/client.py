#!/usr/bin/env python

"""
An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

import socket
import sys
import random
from OFB import *

host = 'localhost'
port = 30006
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

a = int(s.recv(size))
q = int(s.recv(size))
XB = random.randint(1,q-1)
YB = pow(a,XB)%q
YA = int(s.recv(size))
s.send(str(YB))
key = str(pow(YA,XB)%q)
#print key

while 1:
    # read from keyboard
    print '>> ',
    data = sys.stdin.readline()

    if data== '\n':
        break
  
    data = OFB(data,'encrypt', key)
    print 'Decrypt : '+ data
    
    s.send(data)
    s.send('~~~')

    data = s.recv(size)
    
    real_data =''
    real_data += data

    while real_data[len(real_data)-3:len(real_data)]!='~~~':
        data = s.recv(size)
        real_data += data
        
    real_data = OFB(real_data[:len(real_data)-3],'decrypt', key)
    print 'server : ' + real_data.strip()
    
s.close()