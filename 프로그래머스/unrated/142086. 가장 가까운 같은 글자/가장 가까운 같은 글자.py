from collections import defaultdict
def solution(s):
    answer = []
    sDict = defaultdict(int)
    for i in range(len(s)):
        if s[i] not in sDict:
            answer.append(-1)
            sDict[s[i]] = i
        else :
            answer.append(i - sDict[s[i]])
            sDict[s[i]] = i
    return answer