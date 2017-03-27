# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:50:53 2017

@author: exod
"""

def inisialisasi():
    ip = [58,50,42,34,26,18,10,2,
        60,52,44,36,28,20,12,4,
        62,54,46,38,30,22,14,6,
        64,56,48,40,32,24,16,8,
        57,49,41,33,25,17,9,1,
        59,51,43,35,27,19,11,3,
        61,53,45,37,29,21,13,5,
        63,55,47,39,31,23,15,7]
              
    pc1 = [57,49,41,33,25,17,9,
         1,58,50,42,34,26,18,
         10,2,59,51,43,35,27,
         19,11,3,60,52,44,36,
         63,55,47,39,31,23,15,
         7,62,54,46,38,30,22,
         14,6,61,53,45,37,29,
         21,13,5,28,20,12,4]
         
    pc2 = [14,17,11,24,1,5,
         3,28,15,6,21,10,
         23,19,12,4,26,8,
         16,7,27,20,13,2,
         41,52,31,37,47,55,
         30,40,51,45,33,48,
         44,49,39,56,34,53,
         46,42,50,36,29,32]
         
    expansion = [32,1,2,3,4,5,
       4,5,6,7,8,9,
       8,9,10,11,12,13,
       12,13,14,15,16,17,
       16,17,18,19,20,21,
       20,21,22,23,24,25,
       24,25,26,27,28,29,
       28,29,30,31,32,1]
       
    sboxes = { 
     0: [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
     1: [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],
     2: [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
     3: [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ]],
     4: [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
     5: [[ 12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ]],
     6: [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
     7: [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
     }
     
    p_box = [ 16, 7, 20, 21,
      29, 12, 28, 17,
      1, 15, 23, 26,
      5, 18, 31, 10,
      2 , 8, 24, 14,
      32, 27, 3, 9,
      19, 13, 30, 6,
      22, 11, 4, 25 ]
      
    left_rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    ip_inv = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]
          
    return ip, pc1, pc2, expansion, sboxes, p_box, left_rotations, ip_inv
    
def binary2string(b=None):
    return ''.join([chr(int(b[x:x+8], 2)) for x in range(0,len(b),8)])    
    
def string2binary(string):
    return  ''.join(format(ord(x), 'b').zfill(8) for x in string)
    
def hex2binary():
    "{0:0b}".format(int('5f',16))
    return None
    
def IP(i):
    temp_L0_R0 = ''            
    for x in range(len(ip)):
        temp_L0_R0 += bin_plaintext[i][ip[x]-1]
    return temp_L0_R0[:len(ip)/2], temp_L0_R0[len(ip)/2:]
    
def PC1():  
    temp_C_D = ''
    for x in range(len(pc1)):
        temp_C_D += bin_key[pc1[x]-1]
    return temp_C_D[:len(pc1)/2], temp_C_D[len(pc1)/2:]
  
def LEFT_ROT(C0,D0):
    for x in left_rotations:
        C0 = C0[x:]+C0[:x]
        D0 = D0[x:]+D0[:x]    
        K.append(PC2(C0,D0))
    return None
    
def PC2(L, R):         
    K0 = L+R         
    K = ''                    
    for x in range(len(pc2)):
        K += K0[pc2[x]-1]
    return K

def EXPANSI(E0):
    Eks = ''                    
    for x in range(len(expansion)):
        Eks += E0[expansion[x]-1]
    return Eks

def XOR(X, Z):
    c = int(X,2)^int(Z,2)
    c = "{0:0b}".format(c)
    return c
    
def SBOXES(A):    
    count = 0
    B = ''
    for x in range(0,len(A),6):
        a = int(A[x]+A[x+5],2)
        b = int(A[x+1:x+5],2)
        B += "{0:0b}".format(sboxes[count][a][b]).zfill(4)
        count += 1
 
    return B

def P_BOX(B):
    PB = ''                    
    for x in range(len(p_box)):
        PB += B[p_box[x]-1]
    return PB
   
def IP_INV(X):   
    chiper = ''                    
    for x in range(len(ip_inv)):
        chiper += X[ip_inv[x]-1]
    return chiper 
    
def DES(iterasi, iterasi_add):
    L0, R0 = IP(i)
    R.append(R0)
    C0, D0 = PC1()
    LEFT_ROT(C0, D0)
            
    for x in range(16):    
        E = EXPANSI(R[x])
        A = XOR(E,K[iterasi]).zfill(48)
        B = SBOXES(A)
        PB = P_BOX(B)
        if x == 0:
            R.append(XOR(L0,PB).zfill(32))
        else:
            R.append(XOR(R[x-1],PB).zfill(32))
        iterasi += iterasi_add
        
def ENCRYPT(bin_iv):
    iterasi = 0
    iterasi_add = 1

    dummy = bin_plaintext[i]
#    bin_plaintext[i] = XOR(bin_plaintext[i],bin_iv).zfill(64)
    bin_plaintext[i] = bin_iv
    
    DES(iterasi, iterasi_add)
    
    dummy = XOR(dummy,IP_INV(R[16]+R[15])).zfill(64)
    chiper_encrypt.append(dummy)
    return IP_INV(R[16]+R[15])
    
def DECRYPT():
    iterasi = 0
    iterasi_add = 1
    
    dummy = bin_plaintext[i]
    bin_plaintext[i] = bin_iv

    DES(iterasi, iterasi_add)         
    
    dummy = XOR(dummy,IP_INV(R[16]+R[15])).zfill(64)
    text_decrypt.append(dummy)
#    text_decrypt[i]= XOR(text_decrypt[i],bin_iv).zfill(64)
    
    return IP_INV(R[16]+R[15])    
    
def PADDING():
    return None
    
if __name__ == '__main__':
    ip, pc1, pc2, expansion, sboxes, p_box, left_rotations, ip_inv=inisialisasi()
    mode='decrypt'
#    mode = raw_input("encrypt/decrypt : ")
    with open('hasil.txt', 'rb') as f:
        data = f.read()

    if mode == 'encrypt' or mode == 'ENCRYPT' :
        bin_plaintext = ''
#        temp = str(8-len(data)%8)
#        for x in range(len(data)%8,8):
#            data += str(temp)
        data = [data[i:i+8] for i in range(0, len(data), 8) ]
        bin_plaintext = [string2binary(x) for x in data]
    elif mode == 'decrypt' or mode == 'DECRYPT' :
        bin_plaintext=''
        data = [data[i:i+8] for i in range(0, len(data), 8) ]
        bin_plaintext = [string2binary(x) for x in data]
    else:
        print ValueError('Mode salah')

    key = 'inikunci'      
    IV = '12345678'
    bin_iv = string2binary(IV)
    bin_key = string2binary(key)      
    chiper_encrypt = []
    text_decrypt = []    
    
    for i in range(len(bin_plaintext)):
        K = []
        R = []
        if mode == 'encrypt' or mode == 'ENCRYPT' :
            bin_iv = ENCRYPT(bin_iv)
        elif mode == 'decrypt' or mode == 'DECRYPT' :
            bin_iv = DECRYPT()
            
    if mode == 'encrypt' or mode == 'ENCRYPT' :
        h = ''.join(binary2string(x) for x in chiper_encrypt)
        print h
        with open('hasil.txt', 'wb') as f:
            data = f.write(''.join(binary2string(x) for x in chiper_encrypt))
    elif mode == 'decrypt' or mode == 'DECRYPT' :
        h = ''.join(binary2string(x) for x in text_decrypt)
#        valid = True
#        if h[len(h)-1].isdigit():
#            temp = int(h[len(h)-1])
#        for x in range(len(h),len(h)-temp,-1):            
#            if h[x-1].isdigit()==False or int(h[x-1]) != temp:
#                valid = False
#                break
#        else:
#            valid = False
#        if valid == True:
#            h = h[:len(h)-temp]
        
        print h
