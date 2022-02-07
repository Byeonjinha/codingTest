def Njinbub(n):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 2)
        rev_base += str(mod)

    return rev_base[::-1].count('1')

def solution(n):
    tmp = (Njinbub(n))
    while True:
        n+=1
        if tmp == Njinbub(n):
            break
    return n


n= 15

solution(n)