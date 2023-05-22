def solution(numLog):
    prev = 0
    answer = ''
    for idx, num in enumerate(numLog):
        if idx != 0:
            if num == prev + 1:
                answer += "w"
            elif num == prev - 1:
                answer += "s"
            elif num == prev + 10:
                answer += "d"
            elif num == prev - 10:
                answer += "a"
        prev = num
    return answer