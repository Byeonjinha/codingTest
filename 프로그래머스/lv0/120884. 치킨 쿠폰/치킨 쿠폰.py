def solution(chicken):
    answer = 0 
    while chicken >= 10:
        serviceChicken =  10 ** (len(str(chicken))-2)
        chicken -= 10 ** (len(str(chicken))-1)
        chicken += serviceChicken
        answer += serviceChicken
    return answer