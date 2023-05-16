def solution(arr):
    if len(arr) == len(arr[0]):
        return arr
    elif len(arr) > len(arr[0]):
        for i in range(len(arr)):
            arr[i].extend( [0 for _ in range(len(arr) - len(arr[i]))])
    else:
        for i in range(len(arr[0]) - len(arr)):
            arr.append([0 for _ in range(len(arr[i]))])
    return arr