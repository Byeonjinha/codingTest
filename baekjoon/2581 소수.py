import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
if N ==1:
    N=2
sosulist =[]
count = int(0)
for x in range(N,M+1):
    if x>2 and x%2==0:
        continue
    for x2 in range(2, x):
        if x%x2 == 0 :
            count+=1
    if count ==0 :
        sosulist.append(x)
    count=0
if len(sosulist)==0:
    print("-1")
else:
    print(sum(sosulist))
    print(sosulist[0])
