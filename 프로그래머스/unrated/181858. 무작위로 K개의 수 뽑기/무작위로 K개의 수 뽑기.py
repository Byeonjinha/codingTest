def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:
            break
    answer.extend([-1 for _ in range(k - len(answer))] )
    return answer