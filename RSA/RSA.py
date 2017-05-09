# -*- coding: utf-8 -*-
"""
Created on Mon May 08 13:04:53 2017

@author: exod
"""

import numpy as np
import hashlib
#from fractions import gcd

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
        

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primesfrom3to():
        """ Returns a array of primes, p < n """
        n=5000
        assert n>=2
        sieve = np.ones(n/2, dtype=np.bool)
        for i in xrange(3,int(n**0.5)+1,2):
            if sieve[i/2]:
                sieve[i*i/2::i] = False
        z= np.r_[2, 2*np.nonzero(sieve)[0][1::]+1] 
        temp = np.random.randint(95,len(z))
        temp2 = np.random.randint(95,len(z))
        if temp2 == temp:
            temp2 = np.random.randint(95,len(z))
        return z[temp], z[temp2], z
        
def RSA():
    p, q, z = primesfrom3to()
    n = p * q
    m = (p-1)*(q-1)
    e = np.random.randint(1, m)
    
    temp = gcd(e, m)
    while temp != 1:
        e = np.random.randint(1, m)
        temp = gcd(e, m)
        
    d = modinv(e,m);
    return ((long(e), long(n)), (long(d), long(n)))

def encrypt(public, plaintext):
    cipher =  [pow(ord(char),public[0],public[1]) for char in plaintext]
    return cipher

def decrypt(private, ciphertext):
    plain = [chr(pow(char, private[0], private[1])) for char in ciphertext]
    return ''.join(plain)
    
#public key partner di hash
def sign(private_key, text_sign):
    temp = hashlib.md5(str(text_sign))
    signature = encrypt(private_key,temp.hexdigest())
    return signature

#hasil nya di bandingkan dengan nilai hash public key dirinya
def verifikasi(public_key, public_key_partner, signature):
    temp = decrypt(public_key_partner, signature)
    hash_value = hashlib.md5(str(public_key))
    if hash_value.hexdigest() == str(temp):
        return 'verifikasi berhasil'
    else:
        return 'verifikasi gagal'
    
        
    
#if __name__ == "__main__":
#    public_key, peivate_key= RSA()
#    RSA()
#    
    
    
#==============================================================================
# referensi
    # http://ezine.echo.or.id/ezine19/e19.004.txt
    # http://sonyvinda.blogspot.co.id/2010/04/enkripsi-menggunakan-algoritma-rsa.html
    # https://id.wikipedia.org/wiki/RSA#Padding_schemes
    # http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    # # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    # http://octarapribadi.blogspot.co.id/2016/02/enkripsi-dan-dekripsi-menggunakan-rsa.html
#==============================================================================
