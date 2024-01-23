def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a, b)

a, b, c = map(int, input().split())
l = lcm(a, b)
l = lcm(l, c)
print(l)