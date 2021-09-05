from itertools import combinations
def sosulist(n):
    a = [True] * (n + 1)
    m = int(n**0.5)
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False
    answer =([i for i in range(2, n + 1) if a[i] == True])
    return answer
sosulist = sosulist(50000)

def solution(numbers):
    answer = []
    count=0
    p =(list(set(sorted(combinations(list(numbers),3)))))
    print(sosulist)
    for i in p:
        answer.append(sum(list(i)))
    for i in set(sorted(answer)):
        if sosulist.count(i)>0:
            count+=1
    return count

numbers=[1,2,7,6,4,13]
solution(numbers)