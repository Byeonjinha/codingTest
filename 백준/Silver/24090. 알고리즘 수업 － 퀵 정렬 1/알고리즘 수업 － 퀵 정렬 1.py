import sys

sys.setrecursionlimit(811100)
n, k = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
flag = True
def swap(array, a, b):
    global k, flag
    if k == 0:
        return
    k -= 1
    array[a], array[b] = array[b], array[a]
    if k == 0:
        flag = False
        print(array[a], array[b])
        return

def partition(Arr, p, r):
    x = Arr[r]
    i = p - 1
    if k != 0:
        for j in range(p, r):
            if Arr[j] <= x:
                i += 1
                if k != 0:
                    swap(Arr, i, j)
                else:
                    break
        if i + 1 != r:
            swap(Arr, i+1, r)
    return i+1

def quick_sort(Arr, p, r):
    if p < r and k != 0:
        q = partition(Arr, p, r)
        quick_sort(Arr, p, q-1)
        quick_sort(Arr, q+1, r)
quick_sort(a,0,n - 1)

if flag:
    print(-1)