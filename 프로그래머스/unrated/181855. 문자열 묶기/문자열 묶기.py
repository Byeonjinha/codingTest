from collections import defaultdict
def solution(strArr):
    dic = defaultdict(int)
    for i in strArr:
        dic[len(i)] += 1
    dic2 = sorted(dic.items(), key = lambda item: -item[1])
    return dic2[0][1]
    