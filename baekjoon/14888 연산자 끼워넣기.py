import copy
import sys
from itertools import permutations
N=int(sys.stdin.readline())
suzza = list(map(str,sys.stdin.readline().split()))
yeonsan = list(map(int,sys.stdin.readline().split()))
yeonsanlist =[]
for i in range(yeonsan[0]):
    yeonsanlist.append('+')
for i in range(yeonsan[1]):
    yeonsanlist.append('-')
for i in range(yeonsan[2]):
    yeonsanlist.append('*')
for i in range(yeonsan[3]):
    yeonsanlist.append('//')
list1=list(permutations(yeonsanlist,N-1))
list2=[]
k=suzza[0]
list3=[]
for i in list1:
    for j in range(1,N):
        list2.append(str(k))
        list2.append(i[j-1])
        list2.append(suzza[j])
        k=eval(''.join(list2))
        list2.clear()
    list3.append(k)
    k = suzza[0]
print(max(list3),min(list3))
