from math import sqrt
from lib import is_prime

"""This one is very ugly and slow"""

n = 600851475143
c = int(sqrt(n))

while True:
    if is_prime(c) and n % c == 0:
        print(c)
        break
    c -= 1
