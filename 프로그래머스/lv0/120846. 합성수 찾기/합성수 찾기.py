def countDivisor(num):
    count = 0 
    for i in range(1,num+1):
        if num % i == 0 :
            count += 1
    if count >= 3 :
        return True
    else :
        return False
def solution(n):
    answer = 0
    for i in range(4, n+1):
        if countDivisor(i) :
            answer += 1
    return answer