from Crypto.Util import number
from math import *
import os
from base64 import b64encode, b64decode

from itsdangerous import base64_encode

def ExtEuclidean(a, b): #create function
    if b == 0:
        return (a, 1, 0)
    (c, x1, y1) = ExtEuclidean(b, a%b)
    x = y1
    y = x1 - (a//b) * y1
    return (c, x, y) #return the value


def gcdExtended(a, b):
	# Base Case
	if a == 0 :
		return b,0,1
			
	gcd,x1,y1 = gcdExtended(b%a, a)
	
	# Update x and y using results of recursive
	# call
	x = y1 - (b//a) * x1
	y = x1
	
	return gcd,x,y
	

def RSA_keygen(): 
    p = number.getPrime(1024,os.urandom)
    q = number.getPrime(1024,os.urandom)
    N = p*q
    # print(N)
    # print("----")
    # print(log2(N))
    # print("----")
    phiOfn = (p-1)*(q-1) #numbers of prime number between 0-N
    # print(phiOfn)
    e = 65537 # public key
    # d = 1/e mod phiOfn private key
    # if gcd(e,phiOfn) == 1:
    #     print("Good! e is relatively prime to phi(n)")
    # else:
    #     print("Bad! e is not relatively prime to phi(n)")

    _,_,d = ExtEuclidean(phiOfn,e)

    #if ((d*e)%phiOfn == 1):
        #print("correct")


    Public_key = e,N
    Private_key = d,N
    return Public_key,Private_key