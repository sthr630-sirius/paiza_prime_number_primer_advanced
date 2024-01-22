import math
"""
o(nm)~10^8  TLEの場合あり

def  divisor(n):
    d = []
    for i in range(1, n+1):
        if n%i == 0:
            d.append(i)
    print(*d)
"""
def divisor(n):
    d = []
    sqrt_n = int(math.sqrt((n)))
    for i in range(1, sqrt_n+1):
        if n%i == 0:
            d.append(i)
            if i**2 != n:
                d.append(n//i)
    d.sort()
    print(*d)

n = int(input())
for _ in range(n):
    m = int(input())
    divisor(m)
