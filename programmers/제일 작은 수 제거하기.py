def solution(arr):
    arr.remove(arr[arr.index(min(arr))])
    if len(arr) < 1:
        return [-1]
    return arr
