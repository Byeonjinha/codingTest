def solution(num_list, n):
    answer = [[]]
    count = 0 
    for i in num_list:
        if len(answer[-1]) == n :
            answer.append([])
        answer[-1].append(i)
    return answer