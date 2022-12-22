from collections import Counter
def solution(array):
    arrayDic = Counter(array)
    modeValue = 0
    modeNum = 0
    modeArray = []
    for i in arrayDic:
        if modeValue < arrayDic[i]:
            modeArray = []
            modeNum = i
            modeValue = arrayDic[i]
            modeArray.append(i)
        elif modeValue == arrayDic[i]:
            modeArray.append(i)
    if len(modeArray) > 1:
        return -1
    return modeNum