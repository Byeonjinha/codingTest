
n = int(input())
if n % 5 == 0:
    print(n//5)
    exit(0)
k = n // 5
while True:
    if (n - (k * 5)) % 2 == 0:
        break
    else:
        k -= 1
if k < 0:
    print(-1)
else:
    print(k + (n - (k * 5))// 2)