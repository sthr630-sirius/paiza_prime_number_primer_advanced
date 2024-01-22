import math
def IsPrime(n):
    sqrt_n = int(math.sqrt(n))
    if n == 1:
        return False
    for i in range(2, sqrt_n+1):
        if n%i == 0:
            return False
    return True

a, b, c = map(int, input().split())
n_list = [a+b, b+c, c+a]
is_ans = False
for n in n_list:
    if IsPrime(n):
        is_ans = True

if is_ans:
    print("Yes")
else:
    print("No")