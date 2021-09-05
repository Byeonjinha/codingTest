def solution(n):
    p = list(str(n))
    p.sort(reverse=True)
    answer ="".join(p)
    return int(answer)
