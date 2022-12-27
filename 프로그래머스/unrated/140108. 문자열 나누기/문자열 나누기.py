from collections import defaultdict
def solution(s):
    answer = 0
    dic = defaultdict(int)
    first = 0
    notFirst = 0 
    firstStr = ""
    for i in range(len(s)):
        if first == 0 :
            first += 1
            firstStr = s[i]
        else :
            if firstStr == s[i] :
                first += 1
            else :
                notFirst += 1
                if first == notFirst :
                    answer += 1
                    first = 0
                    notFirst = 0
    if first != 0 :
        answer += 1
    return answer