A, B = list(map(int, input().split()))
if B > A :
    A, B = B, A
for i in range(A,0,-1):
    if A%i == 0 and B%i == 0:
        print(i)
        break
for j in range(A, A*B+1):
    if j%A == 0 and j%B == 0:
        print(j)
        break