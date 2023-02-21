import sys
n, k = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
n = len(a)
flag1 = False
for i in range(1, n):
    if k == 0:
        break
    j = i
    tmp = a[i]
    flag2 = False #대소관계가 정렬되어 있는지 확인
    while j > 0 and a[j - 1] > tmp:
        flag2 = True  #대소관계가 정렬되어 있는지 확인 했을 때 정렬 되어있지 않은 경우
        k -= 1  #대소관계가 정렬되어 있는지 확인 했을 때 정렬 되어있지 않은 경우 변화했기 때문에 k - 1
        a[j] = a[j - 1]
        if k == 0:
            flag1 = False
            break
        j -= 1
    if k <= 0:
        break
    if flag2: #대소관계가 정렬되어 있는지 확인 했을 때 정렬 되어있지 않은 경우 재정렬한 k - 1
        k -= 1
    a[j] = tmp
if k == 0:
    print(a[j])
else:
    print(-1)