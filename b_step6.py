n = int(input())
divisor = 0
for i in range(1, n):
    if n%i == 0:
        divisor += i

if divisor == n:
    print("Yes")
else:
    print("No")