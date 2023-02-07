from heapq import heappop, heappush

def solution(n, k, enemy):
    heap = []
    for idx in range(len(enemy)):
        heappush(heap, -enemy[idx])
        n -= enemy[idx]
        if n < 0 and k == 0:
            return idx
        elif n < 0 and k > 0:
            k -= 1
            n -= heappop(heap)
    return idx + 1