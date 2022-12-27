from collections import Counter
def solution(X, Y):
    answer = ''
    xDict = Counter(X)
    yDict = Counter(Y)
    for i in sorted(xDict, reverse = True):
        if i in xDict and i in yDict:
            answer += i*min(xDict[i], yDict[i])
    if answer == '' :
        return "-1"
    if len(Counter(answer)) == 1 and '0' in Counter(answer) :
        return '0'
    return answer