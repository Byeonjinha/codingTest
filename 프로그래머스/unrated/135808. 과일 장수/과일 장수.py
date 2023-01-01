def solution(k, m, score):
    answer = 0
    score.sort()
    while True:
        if m <= len(score) :
            answer += min(score[-m:]) * m
            for i in range(m):
                score.pop()
        else :
            break
    return answer