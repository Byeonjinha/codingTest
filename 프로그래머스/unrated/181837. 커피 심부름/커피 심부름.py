def solution(order):
    answer = 0
    for i in order:
        if "ameri" in i or "anything" in i:
            answer += 4500
        else:
            answer += 5000
    return answer