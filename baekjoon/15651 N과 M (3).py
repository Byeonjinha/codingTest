import sys
from itertools import combinations
N, M=map(int,sys.stdin.readline().split())
list1=[]
for j in range(M):
    for i in range(1,N+1):
        list1.append(str(i))
print(sorted(list1))
p =list(set(list(combinations(list1,M))))
p.sort()
for i in range(len(p)):
    print( ' '.join(p[i]) )
