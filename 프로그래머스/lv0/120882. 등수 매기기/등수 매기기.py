def solution(score):
    sumScore = list(map(sum, score))
    scoreGrade = sorted(list(sumScore), reverse = True)
    answer = []
    for i in sumScore:
        answer.append(scoreGrade.index(i)+1)
    return answer