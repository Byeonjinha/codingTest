def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if len(set(list(str(i))) - {'0', '5'}) == 0:
            answer.append(i)
    if len(answer) == 0: return [-1]
    return answer