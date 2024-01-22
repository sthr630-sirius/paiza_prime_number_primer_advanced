n = int(input())
prime = [True]*(n+1)
prime[0] = False
prime[1] = False

for i in range(2, n+1):
    if prime[i]:
        for j in range(i*2, n+1, i):
            prime[j] = False

for i in range(2, n+1):
    while prime[i]:
        if n%i == 0:
            print(i)
            n = n//i
        else:
            break