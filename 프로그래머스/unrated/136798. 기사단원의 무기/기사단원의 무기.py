def findDivisorCnt(n):
    count = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0 :
            count += 1
            if ( (i**2) != n) : 
                 count += 1
    return count
def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1 ) :
        divisorCnt = findDivisorCnt(i)
        if divisorCnt > limit :
            answer += power
        else :
            answer += divisorCnt
    return answer