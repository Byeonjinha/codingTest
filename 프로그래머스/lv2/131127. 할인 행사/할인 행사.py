from collections import defaultdict
def solution(want, number, discount):
    answer = 0 
    for i in range(len(discount)):
        wantDict = {want[i]: number[i] for i in range(len(want))}
        for j in discount[i:i+10]:
            if j in wantDict:
                wantDict[j] -= 1
                if wantDict[j] == 0:
                    del wantDict[j]
        if len(wantDict) == 0:
            answer += 1
    return answer