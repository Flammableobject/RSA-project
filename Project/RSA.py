from Crypto.Util import number
from math import *
import os



def ExtEuclidean(a, b):  # create function
    if b == 0:
        return (a, 1, 0)
    (c, x1, y1) = ExtEuclidean(b, a % b)
    x = y1
    y = x1 - (a//b) * y1
    return (c, x, y)  # return the value


def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y


def RSA_keygen():
    p = number.getPrime(1024, os.urandom)
    q = number.getPrime(1024, os.urandom)
    N = p*q

    phiOfn = (p-1)*(q-1)  # numbers of prime number between 0-N

    e = 65537

    _, _, d = ExtEuclidean(phiOfn, e)

    d = d % phiOfn
    if(d < 0):
        d += phiOfn

    Public_key = e, N
    Private_key = d, N
    return Public_key, Private_key
