#!/usr/bin/env python 

""" 
An echo server that uses threads to handle multiple clients at a time. 
Entering any line of input at the terminal will exit the server. 
""" 

import select 
import socket 
import sys 
import threading 
import pickle
from RSA import *

class Server:         
    def __init__(self): 
        self.host = ''
        self.port = 50001
        self.backlog = 5 
        self.size = 1024 
        self.server = None 
        self.threads = [] 

    def open_socket(self): 
        try: 
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            self.server.bind((self.host,self.port)) 
            self.server.listen(5) 
        except socket.error, (value,message): 
            if self.server: 
                self.server.close() 
            print "Could not open socket: " + message 
            sys.exit(1) 

    def run(self): 
        self.open_socket() 
        input = [self.server] #,sys.stdin
        running = 1 
        while running: 
            inputready,outputready,exceptready = select.select(input,[],[])

            for s in inputready: 

                if s == self.server: 
                    # handle the server socket 
                    c = Client(self.server.accept()) 
                    c.start() 
                    self.threads.append(c) 

                elif s == sys.stdin: 
                    # handle standard input 
                    junk = sys.stdin.readline() 
                    running = 0 

        # close all threads 

        self.server.close() 
        for c in self.threads: 
            c.join() 

class Client(threading.Thread):
    def __init__(self,(client,address)): 
        threading.Thread.__init__(self) 
        self.client = client 
        self.address = address 
        self.size = 1024 
        self.public_key, self.private_key = RSA()
        self.public_key_partner = pickle.loads(self.client.recv(self.size))
        self.client.send(pickle.dumps(self.public_key))
        
    def run(self): 
        running = 1 
        
        while running: 
            sign_data = pickle.loads(self.client.recv(self.size))
            
            if sign_data: 

#                real_data =''
#                real_data += data

#                while real_data[len(real_data)-3:len(real_data)]!='~~~':
#                    data = self.client.recv(self.size)
#                    real_data += data
                data = pickle.loads(self.client.recv(self.size))    
                print sign_data
                sign_data_in = verifikasi(self.public_key, self.public_key_partner, sign_data)
                print sign_data_in
                
                if sign_data_in == 'verifikasi gagal':
                    continue
                
                real_data = decrypt(self.private_key,data)
                print "client %s : %s" %(self.address, real_data.strip())
                
#                print 'key : '+self.key
                print '>> %s : ' %(self.address, ),
                data = raw_input()
                   
                
                data = encrypt(self.public_key_partner,data)
#                print 'Decrypt : '+ data
                
                self.client.send(pickle.dumps(data))
#                self.client.send('~~~')
            else: 
                self.client.close() 
                running = 0 

if __name__ == "__main__": 
    s = Server()
    print 'waiting client ....\n\n'
    #counter=0
    s.run()