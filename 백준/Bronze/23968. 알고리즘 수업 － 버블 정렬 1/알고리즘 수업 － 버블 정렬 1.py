import sys

n, k = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
flag = True
for i in range(n):
    if flag:
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                k -= 1
                if k == 0:
                    flag = False
                    break
if k == 0:
    print(a[j], a[j + 1])
else:
    print(-1)