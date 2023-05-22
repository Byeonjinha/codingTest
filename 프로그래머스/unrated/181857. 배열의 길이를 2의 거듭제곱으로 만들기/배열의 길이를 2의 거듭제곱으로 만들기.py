def solution(arr):
    k = 0
    while 2 ** k < len(arr):
        k += 1
    arr.extend([0 for _ in range( 2** k - len(arr))])
    return arr