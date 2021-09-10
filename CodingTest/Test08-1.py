import sys
n,k = map(int,sys.stdin.readline().split())
a= list(map(int,sys.stdin.readline().split()))
b= list(map(int,sys.stdin.readline().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[0]<b[0]:
        b.append(a[0])
        a.remove(a[0])
        a.append(b[0])
        b.remove(b[0])
print(sum(a))