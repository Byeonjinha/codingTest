import sys
n, k = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
n = len(a)
flag = True
for i in range(n - 1):
    max = 0
    for j in range(n - i):
        if a[j] > a[max]:
            max = j
    if (n - 1 - i) != max:
        k -= 1
        if k == 0:
            break
        a[n - 1 - i], a[max] = a[max], a[n - 1 - i]
if k == 0:
    print(a[j], a[max])
else:
    print(-1)