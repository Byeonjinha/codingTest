import sys
n=int(sys.stdin.readline())
list1=[]
for i in range(n):
    m=(list(map(int,sys.stdin.readline().split())))
    list1.append(m)
list1.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    print(list1[i][0],list1[i][1])
