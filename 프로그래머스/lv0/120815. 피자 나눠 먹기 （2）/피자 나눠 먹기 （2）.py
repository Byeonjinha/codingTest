def solution(n):
    answer = 0
    while True:
        answer += 1
        if 6* answer % n == 0 :
            return answer
        
    return answer