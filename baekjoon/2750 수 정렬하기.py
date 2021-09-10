import  math
import heapq
import sys
n=int(sys.stdin.readline())
suzza=[[math.inf] for _ in range((10001))]
for i in range(n):
    suzza[i]= [int(sys.stdin.readline())]
heapq.heapify(suzza)
while suzza[0]!=math.inf:
    print(heapq.heappop(suzza)[0])