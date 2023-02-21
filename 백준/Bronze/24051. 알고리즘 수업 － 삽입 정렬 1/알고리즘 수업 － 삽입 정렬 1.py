import sys
n, k = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
n = len(a)
flag1 = False
for i in range(1, n):
    if k == 0:
        break
    j = i
    tmp = a[i]
    flag2 = False
    while j > 0 and a[j - 1] > tmp:
        flag2 = True
        k -= 1
        a[j] = a[j - 1]
        if k <= 0:
            flag1 = False
            break
        j -= 1
    if k <= 0:
        break
    if flag2:
        k -= 1
    a[j] = tmp
if k == 0:
    print(a[j])
else:
    print(-1)