from math import *

def fib(n, memo = {}):
    """Returns the n:th Fibonacci number."""
    if n in memo:
        return memo[n]
    elif n > 1:
        return memo.setdefault(n, fib(n - 1) + fib(n - 2));
    return n

def is_prime(n):
    """Checks if a number is prime."""
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True
