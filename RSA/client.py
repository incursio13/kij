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
    # mengirim data
    print '>> ',
    data = sys.stdin.readline()

    if data== '\n':
        break
    
    sign_data = sign(private_key, public_key_partner)
    data = encrypt(public_key_partner, data)

    s.sendall(pickle.dumps(sign_data))
    s.sendall(pickle.dumps(data))
    s.send('~~~')

    #verifikasi signature
    sign_data = pickle.loads(s.recv(size))        
    sign_data_in = verifikasi(public_key, public_key_partner, sign_data)
    
    print '# public key : '+str(public_key_partner)
    print '# '+sign_data_in    
    if sign_data_in == 'verifikasi gagal':
        s.send('')
        continue
    
    #menerima data
    data = s.recv(size)
    real_data =''
    real_data += data

    while real_data[len(real_data)-3:len(real_data)]!='~~~':
        data = s.recv(size)
        real_data += data
        
    data = pickle.loads(real_data)        
    real_data = decrypt(private_key,data)
    print '# server : ' + real_data.strip()
    print '\n'
    
s.close()

