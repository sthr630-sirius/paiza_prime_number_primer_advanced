def gcd (a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b, c = map(int, input().split())
print(gcd(gcd(a, b), c))