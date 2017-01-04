from math import *

def fib(n, memo = {}):
    """Returns the n:th Fibonacci number."""
    if n in memo:
        return memo[n]
    elif n > 1:
        return memo.setdefault(n, fib(n - 1) + fib(n - 2))
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

def is_palindrome(n):
    """Checks if the argument is a palindrome."""
    ns = str(n)
    for i in range(0, len(ns) // 2):
        if ns[i] != ns[len(ns) - 1 - i]: return False
    return True

def sumn(n):
    m = n * (n + 1) / 2
    return m * m

def sumn_pow2(n):
    """Returns the sum of the first n squared integers."""
    return (n * (n + 1) * (2 * n + 1)) / 6
