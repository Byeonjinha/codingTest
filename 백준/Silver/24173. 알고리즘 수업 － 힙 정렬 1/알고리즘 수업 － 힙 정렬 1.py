import sys

sys.setrecursionlimit(10 ** 4)
n, k = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
flag = True


def heapify(array, parent, size):
    global k, flag
    if k == 0:
        flag = False
        return
    smallest = parent
    left = (2 * parent) + 1
    right = (2 * parent) + 2

    if (left < size) and (array[left] < array[smallest]): smallest = left
    if (right < size) and (array[right] < array[smallest]): smallest = right
    if smallest != parent:
        k -= 1

        if k == 0:
            flag = False
            print(min(array[smallest], array[parent]), max(array[smallest], array[parent]))
            return
        array[parent], array[smallest] = array[smallest], array[parent]
        heapify(array, smallest, size)


def build_min_heap(a, n):
    for i in range((n // 2) - 1, -1, -1):
        heapify(a, i, n)


def heap_sort(a):
    global n, k, flag
    if k == 0:  # k 가 0이면 정렬 종료.
        flag = False
        return
    build_min_heap(a,n)

    for j in range(n - 1, 0, -1):
        if k == 0:
            flag = False
            break
        k -= 1
        if k == 0:
            print(min(a[0], a[j]), max(a[0], a[j]))
            flag = False
            break
        a[0], a[j] = a[j], a[0]
        heapify(a, 0, j)


heap_sort(a)  # 배열삽입

if flag:
    print(-1)
