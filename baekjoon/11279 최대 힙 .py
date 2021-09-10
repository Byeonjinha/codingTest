import heapq
import sys
bae10=[]
heapq.heapify(bae10)
N =int(sys.stdin.readline())
for i in range(N):
    x = int(sys.stdin.readline())
    if x==0 and len(bae10)==0:
        print("0")
        continue
    if x==0:
        print(heapq.heappop(bae10)*-1)

    elif x!=0 :
        heapq.heappush(bae10,-x)
