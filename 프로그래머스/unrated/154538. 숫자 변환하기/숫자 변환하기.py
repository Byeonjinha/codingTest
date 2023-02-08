import math
def solution(x, y, n):
    xList = [math.inf for i in range(1000002)]
    xList[x] = 0
    for i in range(1, len(xList)-1):
        if i%2 == 0 :
            xList[i] = min(xList[i], xList[i//2]+1)
        if i%3 == 0 :
            xList[i] = min(xList[i], xList[i//3]+1)
        if i-n >= 0:
            xList[i] = min(xList[i], xList[i-n]+1)
    if xList[y] == math.inf:
        return -1
    return xList[y]