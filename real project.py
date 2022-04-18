# Pre generated primes
from math import *
from primeGenerator import *
from ED import *
from EDbitSeq import *
import random

first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
					31, 37, 41, 43, 47, 53, 59, 61, 67,
					71, 73, 79, 83, 89, 97, 101, 103,
					107, 109, 113, 127, 131, 137, 139,
					149, 151, 157, 163, 167, 173, 179,
					181, 191, 193, 197, 199, 211, 223,
					227, 229, 233, 239, 241, 251, 257,
					263, 269, 271, 277, 281, 283, 293,
					307, 311, 313, 317, 331, 337, 347, 349]


#accept input
i = input("please select to decrypt or encrpyt('type e or d): ")
if i == 'e':
    #accept text string input for encrypt
    s = input("please input text: ")
    #seperate input into element and turn alphabet into ascii
    #list for ascii
    a = []
    for i in range(len(s)):
        a.append(ord(s[i]))
    #Convert into binary
    for i in range(len(a)):
        a[i] = bin(a[i])[2:].zfill(8)
    #merge all the elements to get bit sequence
    a[0:len(a)] = [''.join(a[0 :len(a)])]
    b = a[0] #b = bit sequence
    #keygen 
    
        

    
