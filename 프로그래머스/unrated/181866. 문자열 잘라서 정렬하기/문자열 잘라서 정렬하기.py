def solution(myString):
    a =  sorted(myString.split("x"))
    while "" in a:
        a.remove("")
    return a