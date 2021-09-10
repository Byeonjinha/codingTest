import sys
list=[]
n= int(sys.stdin.readline())
for i in range(n):
    m= int(sys.stdin.readline())
    list.append(m)
list.sort(reverse=True)
for i in list:
    print(i,end=' ')