import sys
import math
N, K =  map(int,sys.stdin.readline().split())
count = int(0)
Alist=[]
for i in range(0,N):
    A = int(sys.stdin.readline())
    Alist.append(A)
Alist.sort(reverse=True)
for i2 in range(0,len(Alist)):
    if K < Alist[i2]:
        1==1
    elif K==Alist[i2]:
        count = count + int(K / Alist[i2])
        break
    else:
        count = count + int(math.floor(K / Alist[i2]))
        K=K%Alist[i2]

    if K==0:
        break
print(count)