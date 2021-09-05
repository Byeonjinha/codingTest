import sys
N = int(sys.stdin.readline())
x = int(0)
y = int(2)
result=[]
while N!=1:
    if N%y==0:
        N=N/y
        result.append(y)
    elif N!=1 and N%y!=0:
        y= y+1
for x in range(0,len(result)):
    print(result[x])