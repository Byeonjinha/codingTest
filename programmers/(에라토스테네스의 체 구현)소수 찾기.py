
def solution(n):
    a = [True] * (n + 1)
    m = int(n**0.5)
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False
    answer =(len([i for i in range(2, n + 1) if a[i] == True]))
    return answer

'''
소수 개수를 return 함
len 을 빼면 소수 list return 함
'''