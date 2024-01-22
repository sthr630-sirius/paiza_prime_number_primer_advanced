import math
def IsPrime(n):
    sqrt_n = int(math.sqrt(n))
    if n == 1:
        return False
    else:
        for i in range(2, sqrt_n+1):
            if n%i == 0:
                return False
        return True

n = int(input())
sqrt_n = math.sqrt(n)

is_near_prime = False

if IsPrime(n-1):
    is_near_prime = True
elif IsPrime(n+1):
    is_near_prime = True

if IsPrime(n):
    is_near_prime = False

if is_near_prime:
    print("Yes")
else:
    print("No")