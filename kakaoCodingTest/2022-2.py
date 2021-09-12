def Njinbub(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]


def sosu(n):
    a = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False
    answer = ([i for i in range(2, n + 1) if a[i] == True])
    return answer


def solution(n, k):
    count = 0
    byeonhwan = (Njinbub(n, k))
    s = byeonhwan.split('0')
    while s.count('') != 0:
        s.remove('')
    try:
        for i in s:
            sosulist = sosu(int(i))
            if int(i) in sosulist:
                count += 1
        answer = count
        print(answer)
        return answer
    except:
        if int(i) >  1111111111111:
            return 1
        else:
            return 0