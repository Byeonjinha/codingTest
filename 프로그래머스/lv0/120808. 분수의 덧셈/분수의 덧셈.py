import copy
def findDivisor(num):
    divisor = []
    while num != 1 :
        for i in range(2,num+1):
            if num % i == 0 :
                num //= i
                divisor.append(i)
                break
    return divisor

def solution(denum1, num1, denum2, num2):
    answer = []
    sumDeNum = denum1 * num2 + denum2 * num1
    sumNum = num1 * num2
    sumDeNumDevisor = findDivisor(sumDeNum)
    sumNumDevisor = findDivisor(sumNum)
    
    tmpDeNumDevisor =  copy.deepcopy(sumDeNumDevisor)
    print(sumDeNumDevisor, sumNumDevisor)
    for i in sumDeNumDevisor:
        if i in sumNumDevisor :
            tmpDeNumDevisor.remove(i)
            sumNumDevisor.remove(i)
    newDenum = 1
    newNum = 1
    for j in tmpDeNumDevisor :
        newDenum *= j
    for k in sumNumDevisor :
        newNum *= k
    return [newDenum, newNum]