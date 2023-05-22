def solution(rank, attendance):
    idx = [i for i in range(len(rank))]
    answer = list(zip(rank, attendance, idx))
    answer.sort(key = lambda x: (-x[1], x[0]))
    print(answer)
    return sum([answer[0][2] *10000, answer[1][2] *100, answer[2][2]] )