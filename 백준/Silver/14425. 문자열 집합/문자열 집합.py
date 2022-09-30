import sys
N, M = list(map(int, sys.stdin.readline().split()))
strDic = {}
count = 0
for i in range(N):
    strDic[sys.stdin.readline()] = i
for j in range(M):
    if sys.stdin.readline() in strDic:
        count += 1
print(count)