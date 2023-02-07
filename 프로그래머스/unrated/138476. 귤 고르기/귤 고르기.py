from collections import Counter
from heapq import heappush, heappop
def solution(k, tangerine):
    answer = 0
    heap = []
    tangerineDict = Counter(tangerine) 
    for tangerineCount in tangerineDict:
         heappush(heap, -tangerineDict[tangerineCount])
    while heap and k > 0 :
        a = heappop(heap)
        k += a
        answer += 1
    return answer