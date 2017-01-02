#!/bin/python
from lib import is_palindrome

# Brute force.

curmax = 0
for n1 in range(100, 1000):
    for n2 in range(100, 1000):
        n = n1 * n2
        if is_palindrome(n) and n > curmax:
            curmax = n

print(curmax)
