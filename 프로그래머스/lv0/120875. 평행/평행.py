from itertools import permutations
def solution(dots):
    answer = 0
    answerList = []
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            if float(float(dots[i][0]) - float(dots[j][0])) / (float(dots[i][1]) - float(dots[j][1])) in answerList:
                return 1
            else:
                answerList.append(float(float(dots[i][0]) - float(dots[j][0])) / (float(dots[i][1]) - float(dots[j][1])))
    return 0