import sys

def asum(start , end ,key):
    if start >  end:
        return 0
    mid = (start+end)//2
    if a[mid] == key:
        return 1
    elif a[mid] > key:
        return asum(start, mid-1,key)
    elif a[mid] < key:
        return asum(mid+1, end, key)

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
answer = 0
a.sort()

for num in a:
    if (num*2) ==x:
        continue

    answer += asum(0,len(a)-1,x-num)

print(answer//2)