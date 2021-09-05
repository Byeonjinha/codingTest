import sys
list=[]
n= int(sys.stdin.readline())
for i in range(n):
    m= sys.stdin.readline().split()
    list.append(m)
list.sort(key=lambda x:x[1])
for i in list:
    print(i[0],end=' ')