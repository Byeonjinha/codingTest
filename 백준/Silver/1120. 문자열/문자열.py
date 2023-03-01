import sys
import math

A, B = sys.stdin.readline().strip().split()
answer = math.inf


def checkGapCount(A, B):
    gap = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            gap += 1
    return gap


for i in range(len(B) - len(A) + 1):
    answer = min(answer, checkGapCount(A, B[i:len(A) + i]))
    # A 길이 만큼 B를 단순법으로 비교해 문자열의 차이를 카운터한다.
print(answer)
