import heapq

def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        piece = arr[s:e+1]
        heapq.heapify(piece)
        if max(piece) <= k:
            answer.append(-1)
            continue
        while piece:
            minv = heapq.heappop(piece)
            if minv > k:
                answer.append(minv)
                break
                
    return answer