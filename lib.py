def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    elif n > 1:
        return memo.setdefault(n, fib(n - 1) + fib(n - 2));
    return n
