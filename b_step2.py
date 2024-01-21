def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a, b)

n = int(input())
n_list = [int(input()) for _ in range(n)]

g = n_list[0]
l = n_list[0]
for i in range(1, n):
    g = gcd(g, n_list[i])
    l = lcm(l, n_list[i])

print(g, l)