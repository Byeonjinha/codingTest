from itertools import permutations
def sosulist(n):
    a = [True] * (n + 1)
    m = int(n**0.5)
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False
    answer =([i for i in range(2, n + 1) if a[i] == True])
    return answer
sosulist = sosulist(1111111)

def solution(numbers):
    answer = 0
    for i in range(1,7):
        p =(list(set(permutations(list(numbers),i))))
        for i2 in p:
            if i2[0]!='0' and int(''.join(list(i2))) in sosulist:
                answer+=1

    print(answer)
    return answer
