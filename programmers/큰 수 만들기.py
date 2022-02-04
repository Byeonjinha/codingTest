from itertools import combinations
def solution(number, k):
    list_1 = list(combinations(list(number), len(number)-k ))
    max = -1
    for i in range(len(list_1)):
        if max < int(''.join(list(list_1[i]))):
            max = int(''.join(list(list_1[i])))
    answer = max

    return answer

number = "4177252841"
k = 4
solution(number,k)