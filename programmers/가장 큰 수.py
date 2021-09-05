def solution(numbers):
    p=list(map(str,numbers))
    p.sort(key= lambda x:x*3,reverse=True)
    if int("".join(p))==0:
        return '0'
    return "".join(p)

numbers= [0,0]
solution(numbers)