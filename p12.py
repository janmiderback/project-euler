#!/bin/python
from lib import *
from functools import *

n = 1
maxndiv = 0
ps = primes(1000)  # Should be enough with primes < 1000
while maxndiv < 500:
    s = sumn(n)
    pfacs = primefac(s, ps)
    ndiv = 1
    for pf in pfacs:
        ndiv *= (pf[1] + 1)
    if ndiv > maxndiv:
        maxndiv = ndiv
        print(n, s, ndiv)
    n += 1
