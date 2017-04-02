#!/bin/python

N = 1000

# Brute force
for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        for c in range(b + 1, N + 1):
            if (a + b + c == N) and (a * a + b * b == c * c):
                print(a * b * c)
