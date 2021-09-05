def solution(n):
    print(Njinbub(n))
    answer = ''
    return answer



def Njinbub(n):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    return rev_base[::-1]


n=3
solution(n)