import sys
from collections import Counter
n=int(sys.stdin.readline())
list1=[]
for i in range(n):
    m=int(sys.stdin.readline())
    list1.append(m)
list1.sort()
bingap=Counter(list1).most_common()


print(round(sum(list1) / n))
print(list1[n//2])
if len(bingap)>1 and bingap[0][1]==bingap[1][1]:
    print(bingap[1][0])
else:
    print(bingap[0][0])
print(max(list1)-min(list1))