def solution(k, score):
    answer = []
    tmpArray = []
    for i in score:
        if len(tmpArray) != k:
            tmpArray.append(i)
            answer.append(min(tmpArray))
        else :
            tmpArray.append(i)
            tmpArray.remove(min(tmpArray))
            answer.append(min(tmpArray))
    return answer