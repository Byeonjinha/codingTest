from string import ascii_lowercase
from string import ascii_uppercase

lista = ascii_lowercase
listA = ascii_uppercase
relist =[]
def solution(s, n):
    for i in s:
        if i in lista:
            if ord(i) + n > 122:
                relist.append(chr(ord(i) + n - 26))
            else:
                relist.append(chr(ord(i) + n))
        elif i in listA:
            if ord(i)+n>90:
                relist.append(chr(ord(i)+n-26))
            else:
                relist.append(chr(ord(i) +n))
        else:
            relist.append(" ")
    answer = "".join(relist)
    return answer

