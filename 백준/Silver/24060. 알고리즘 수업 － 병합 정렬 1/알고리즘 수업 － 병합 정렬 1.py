import sys

n, k = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
flag = True
def merge(a, p, q, r):
    global k, flag
    i = p
    j = q + 1
    t = 1
    while i <= q and j <= r:
        # print(a)
        if a[i] <= a[j]:
            buff[t] = a[i]
            t += 1
            i += 1
        else:
            buff[t] = a[j]
            t += 1
            j += 1
    while i <= q:
        # print(a)
        buff[t] = a[i]
        t += 1
        i += 1
    while j <= r:
        buff[t] = a[j]
        t += 1
        j += 1
    i = p
    t = 1
    while i <= r: #결과를 배열에 저장
        a[i] = buff[t]
        i += 1
        t += 1
        k -= 1
        if k == 0:
            print(buff[t - 1])
            flag = False
            break

def merge_sort(a, p, r) -> None:
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

buff = [None] * (n * 2)
merge_sort(a, 0, n - 1)
if flag:
    print(-1)