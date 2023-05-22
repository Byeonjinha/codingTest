def solution(arr):
    stk = []
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        else:
            while stk[-1] >= arr[i]:
                stk.pop()
                if len(stk) == 0:
                    break
            stk.append(arr[i])
    return stk