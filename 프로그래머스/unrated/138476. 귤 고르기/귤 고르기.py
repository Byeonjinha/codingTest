from collections import Counter
def solution(k, tangerine):
    tDict = Counter(tangerine)
    tDict = sorted(tDict.items(), key=lambda x: -x[1])
    answer = 0
    for _,count in tDict:
        k -= count
        answer += 1
        if k <= 0:
            break
    return answer