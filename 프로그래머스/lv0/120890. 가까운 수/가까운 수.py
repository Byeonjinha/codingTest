def solution(array, n):
    result = 99999
    for i in array:
        if abs(n-result) > abs(n-i):
            result = i
        elif abs(n-result) == abs(n-i):
            result = min(result, i)
    return result