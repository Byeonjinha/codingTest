from collections import Counter
def solution(s):
    answer = ''
    sDic = Counter(s)
    for i in sDic :
        if sDic[i] == 1:
            answer += i
    return ''.join(sorted(answer))