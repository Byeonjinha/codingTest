import heapq

def solution(scoville, K):
    answer = 0
    under_k=[]
    heapq.heapify(scoville)
    for v in scoville:
        if K>=v:
            heapq.heappush(under_k,v)
    while len(under_k)!=0:
        a=heapq.heappop(under_k)
        b=heapq.heappop(under_k)
        if K<=a+b*2:
            answer+=1
        else:
            heapq.heappush(under_k,a+b*2)
            answer+=1
        if len(under_k)==0 and under_k[0]<K:
            return -1
    return answer