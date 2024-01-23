def divisor(n):
    d_sum = 0
    for i in range(1, n):
        if n%i == 0:
            d_sum += i
    return d_sum

a, b = map(int, input().split())
if divisor(a) > divisor(b):
    print("paiza")
elif divisor(a) < divisor(b):
    print("izapa")
else:
    print("draw")
