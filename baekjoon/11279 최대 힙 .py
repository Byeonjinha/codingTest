from collections import deque
import sys
bae10 = []

N =int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())
    if x==0 and len(bae10)==0:
        print("0")
        continue
    if x==0:
        print(max(bae10))
        bae10.remove(max(bae10))
    elif x!=0 :
        bae10.append(x)
