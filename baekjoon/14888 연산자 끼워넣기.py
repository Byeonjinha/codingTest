import sys
i  = int(sys.stdin.readline())
if i==0:
    print(1)
else:
    n=1
    while i!=1:
       n*=i
       i-=1
    print(n)