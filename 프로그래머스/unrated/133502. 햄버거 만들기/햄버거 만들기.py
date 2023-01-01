def solution(ingredient):
    answer = 0
    answerArray = []
    for i in ingredient:
        answerArray.append(i)
        if len(answerArray) >= 4:
            if answerArray[-4] == 1 and answerArray[-3] == 2 and answerArray[-2] == 3 and answerArray[-1] == 1 :
                answerArray.pop()
                answerArray.pop()
                answerArray.pop()
                answerArray.pop()
                answer += 1   
    return answer