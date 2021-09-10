from itertools import combinations
import sys
N, M=map(int,sys.stdin.readline().split())
list1=[]
for i in range(1,N+1):
    list1.append(i)
p =(list(combinations(list1,M)))

for i in range(len(p)):
    for j in range(len(p[i])-1):
        print(p[i][j],end=' ')
    print(p[i][-1])