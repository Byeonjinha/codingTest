import copy
def solution(arr):
    answer = -1
    prev = []
    while prev != arr:
        prev = copy.deepcopy(arr)
        answer+= 1
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] >= 50:
                arr[i] //= 2
            elif arr[i] % 2 == 1 and arr[i] < 50:
                arr[i] = arr[i] * 2 + 1
    return answer