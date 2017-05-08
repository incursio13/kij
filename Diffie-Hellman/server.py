#!/usr/bin/env python 

""" 
An echo server that uses threads to handle multiple clients at a time. 
Entering any line of input at the terminal will exit the server. 
""" 

import select 
import socket 
import sys 
import threading 
import random
import numpy as np
from OFB import *

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
    def primesfrom3to(self):
        # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
        """ Returns a array of primes, p < n """
        n=5000
        assert n>=2
        sieve = np.ones(n/2, dtype=np.bool)
        for i in xrange(3,int(n**0.5)+1,2):
            if sieve[i/2]:
                sieve[i*i/2::i] = False
        z= np.r_[2, 2*np.nonzero(sieve)[0][1::]+1] 
        temp = random.randint(95,len(z))
        self.q= z[temp]
        
    def __init__(self,(client,address)): 
        threading.Thread.__init__(self) 
        self.client = client 
        self.address = address 
        self.size = 1024 
        
        self.a = 3
        self.primesfrom3to()
        self.client.send(str(self.a)) 
        self.client.send(str(self.q))
        self.XA = random.randint(1,self.q-1)
        self.YA = pow(self.a,self.XA)%self.q
        self.client.send(str(self.YA))
        self.YB = int(self.client.recv(self.size))
        self.key = str(pow(self.YB,self.XA) % self.q)
        
    def run(self): 
        running = 1 
        
        while running: 
            data = self.client.recv(self.size) 
            if data: 

                real_data =''
                real_data += data

                while real_data[len(real_data)-3:len(real_data)]!='~~~':
                    data = self.client.recv(self.size)
                    real_data += data
                
                real_data = OFB(real_data[:len(real_data)-3],'decrypt',self.key)
                print "client %s : %s" %(self.address, real_data.strip())
                
                print 'key : '+self.key
                print '>> %s : ' %(self.address, ),
                data = raw_input()
                   
                
                data = OFB(data,'encrypt', self.key)
                print 'Decrypt : '+ data
                
                self.client.send(data) 
                self.client.send('~~~')
            else: 
                self.client.close() 
                running = 0 

if __name__ == "__main__": 
    s = Server()
    print 'waiting client ....\n\n'
    #counter=0
    s.run()