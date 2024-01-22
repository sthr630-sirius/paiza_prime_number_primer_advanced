import math
n = int(input())
sqrt_n = int(math.sqrt(n))
is_prime = True

for i in range(2, sqrt_n+1):
    if n%i == 0:
        is_prime = False

if n == 1:
    is_prime = False

if is_prime:
    print("Yes")
else:
    print("No")