def solution(n):
    answer = 1
    count = 1
    while True :
        answer += 1
        count *= answer
        if count > n :
            return answer - 1
    return answer