import math
"""
def IsPrime(n):
    if n == 1:
        return False
    else:
        sqrt_n = int(math.sqrt(n))
        for i in range(2, sqrt_n+1):
            if n%i == 0:
                return False
        return True

a, b = map(int, input().split())
is_nothing = True

for i in range(a, b+1):
    if IsPrime(i):
        print(i)
        is_nothing = False

if is_nothing:
    print("Nothing")
"""
a, b = map(int, input().split())

prime = [True] * (b+1)
prime[0] = False
prime[1] = False

sqrt_b = int(math.sqrt(b))

for i in range(2, b+1):
    if prime[i]:
        for k in range(i*2, b+1, i):
            prime[k] = False

is_nothing = True
for i in range(a, b+1):
    if prime[i]:
        print(i)
        is_nothing = False
if is_nothing:
    print("Nothing")