#!/usr/bin/env python

"""
An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

import socket
import sys
import pickle
from RSA import *

host = 'localhost'
port = 50001
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
public_key, private_key = RSA()
s.send(pickle.dumps(public_key))
public_key_partner = pickle.loads(s.recv(size))


while 1:
    # read from keyboard
    print '>> ',
    data = sys.stdin.readline()

    if data== '\n':
        break
    
    sign_data = sign(private_key, public_key_partner)
    data = encrypt(public_key_partner, data)

    print 'public key : '+str(public_key_partner)
    s.send(pickle.dumps(sign_data))
    s.send(pickle.dumps(data))

    data = pickle.loads(s.recv(size))
    
        
    real_data = decrypt(private_key,data)
    print '# server : ' + real_data.strip()
    print '\n'
    
s.close()

