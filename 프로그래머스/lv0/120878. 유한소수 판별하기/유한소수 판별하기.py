def findDivisor(n):
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0 :
                if i == 2 or i == 5 :
                    continue
                else :
                    return False
                break
    return True
def findDiversorArray(n):
    array = []
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0 :
                n //= i
                array.append(i)
                break  
    return array
def solution(a, b):
    aArray = findDiversorArray(a)
    bArray = findDiversorArray(b)
    for i in aArray:
        if i in bArray:
            bArray.remove(i)
    for i in list(set(bArray)) :
        if i != 2 and i != 5:
            return 2
    return 1