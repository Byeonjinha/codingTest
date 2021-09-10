import sys
sum=0
sum1=[]
n = sys.stdin.readline().strip()
for i in range(0,1000000):
    for j in str(i):
        sum+=int(j)
    sum+=int(i)
    if int(n)==sum:
        sum1.append(i)
        break
    sum=0
if len(sum1)<1:
    print(0)
else:
    print(sum1[0])