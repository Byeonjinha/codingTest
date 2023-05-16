def solution(arr):
    if 2 not in arr: return [-1]
    start = arr.index(2)
    end = len(arr) - list(reversed(arr)).index(2)
    answer = arr[start:end]
    return answer