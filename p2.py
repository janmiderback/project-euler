from lib import fib

limit = 4000000
v = 0
n = 0
sum = 0

while True:
    v = fib(n)
    if v <= limit:
        sum += v
        n += 3
    else: break

print(sum)
