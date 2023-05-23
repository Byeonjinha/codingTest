def solution(arr, idx):
    for i, num in enumerate(arr):
        if num == 1 and i>= idx : return i
    return -1