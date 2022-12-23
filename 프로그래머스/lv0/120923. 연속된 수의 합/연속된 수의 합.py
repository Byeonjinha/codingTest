def solution(num, total):
    answer = []
    numArray = [i for i in range(-1001,1001)]
    for i in range(2002):
        if sum(numArray[i:i+num]) == total :
            return numArray[i:i+num]
    return answer