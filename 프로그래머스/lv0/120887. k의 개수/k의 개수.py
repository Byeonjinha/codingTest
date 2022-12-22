from collections import Counter
def solution(i, j, k):
    answer = 0
    for i in range(i,j+1):
        answer += Counter(str(i))[str(k)]
    return answer