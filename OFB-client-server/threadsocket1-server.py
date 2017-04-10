#!/usr/bin/env python 

""" 
An echo server that uses threads to handle multiple clients at a time. 
Entering any line of input at the terminal will exit the server. 
""" 

import select 
import socket 
import sys 
import threading 
from OFB import *

class Server: 
    def __init__(self): 
        self.host = 'localhost'
        self.port = 50012
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

    def run(self): 
        running = 1 
        print 'waiting client ....\n\n'
        while running: 
            data = self.client.recv(self.size) 
            if data: 
                data = OFB(data,'decrypt')
                temp_data2 = int(data.split(',')[0])
                
                looping=len(data.split(', ')[1])
                real_data =data.split(', ')[1]             
                
                while looping<temp_data2:
                    data = self.client.recv(buff)                    
                    looping=looping+len(data)
                    real_data += data.strip()
                
                
                print "client %s : %s" %(self.address, real_data.strip())
                
                print '>> ',
                data = sys.stdin.readline()
                
                data = str(len(data))+", "+ data    
                data = OFB(data,'encrypt')
                print 'Decrypt : '+ data
                
                self.client.send(data) 
                
            else: 
                self.client.close() 
                running = 0 

if __name__ == "__main__": 
    s = Server()
    #counter=0
    s.run()