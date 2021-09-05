from itertools import combinations
def solution(numbers):
    answer=[]
    for i in (list(set(combinations(numbers,2)))):
        answer.append(sum(i))
        answer=sorted(list(set(answer)))
    return answer
