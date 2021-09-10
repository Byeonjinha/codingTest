import sys
n=int(sys.stdin.readline())
list1=[]
for i in range(n):
    m=sys.stdin.readline().split()
    list1.append([int(m[0]),m[1]])
list1.sort(key=lambda x:x[0])
for i in range(n):
    print(list1[i][0],list1[i][1])
