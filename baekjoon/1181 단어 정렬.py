import sys
n=int(sys.stdin.readline())
list1=[]
list2=[]
for i in range(n):
    m = sys.stdin.readline().strip()
    list1.append(m)
list1=list(set(list1))

for i in range(len(list1)):
    list2.append([len(list1[i]),list1[i]])
list2.sort(key=lambda x:(x[0],x[1]))
for i in range(len(list2)):
    print(list2[i][1])
