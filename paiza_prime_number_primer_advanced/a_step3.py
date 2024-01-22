import math

a, b = map(int, input().split())

prime = [True] * (b+1)
prime[0] = False
prime[1] = False

sqrt_b = int(math.sqrt(b))

for i in range(2, b+1):
    if prime[i]:
        for k in range(i*2, b+1, i):
            prime[k] = False

ans = 0

for i in range(a, b+1):
    if prime[i]:
        ans += 1

print(ans)