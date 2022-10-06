import sys

N= int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
answer = 0
for i in range(len(A)):
    peoplesCount = A[i] - B
    answer += 1
    if peoplesCount > 0 :
        if peoplesCount % C == 0:
            answer += peoplesCount // C
        else:
            answer += (peoplesCount // C)+1
print(answer)