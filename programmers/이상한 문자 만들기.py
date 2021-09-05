def solution(s):
    s=s.split(" ")
    s2=[]
    for i in s:
        for i2 in range(0,len(i)):
            if i2%2!=0:
                s2.append(i[i2].lower)
            else:
                s2.append(i[i2].upper())
        s2.append(" ")
    s2.pop()
    answer = ''.join(s2)
    print(answer)
    return answer

s="power overwhelming"
solution(s)