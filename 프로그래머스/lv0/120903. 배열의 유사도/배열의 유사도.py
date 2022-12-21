def solution(s1, s2):
    result = 0 
    for i in s1:
        if i in s2:
            result += 1
    return result