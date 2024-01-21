import math
n = int(input())
sqrt_n = int(math.sqrt(n))
prime =  [True]*(n+1)
prime[0] = False
prime[1] = False

ans = 0
max_prime_count = 0
counter = 0

for i in range(2, sqrt_n+1):
    if prime[i]:
        for j in range(i*2, n+1, i):
            prime[j] = False

#for i in range(1, n+1):
#    print(f"i:{i}", prime[i])

for i in range(2, n+1):
    counter = 0
    while prime[i]:
        if n%i == 0:
            counter += 1
            n = n // i
        else:
            if counter >= max_prime_count:
                max_prime_count = counter
                ans = i
            break

print(ans)