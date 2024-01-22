import math
def IsPrime(n):
    if n == 1:
        return False
    else:
        sqrt_n = int(math.sqrt(n))
        for i in range(2, sqrt_n+1):
            if n%i == 0:
                return False
        return True

n = int(input())

for i in reversed(range(n+1)):
    if IsPrime(i):
        print(i)
        break