from lib import *

# By experimenting it can be found that the 10001th prime is in the range [2, 200000].
LIMIT = 200000
p = primes(LIMIT)
print(p[10000])
