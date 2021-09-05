from collections import deque
def solution(n, m):
    temp=0
    if n<m:
        temp=n
        n=m
        m=temp

    n,m = insoobunhae(n,m)
    yacksoo=deque()
    baesoo=n+m
    yackso=1
    baeso=1
    for i in list(n):
        for j in list(m):
            if i==j:
                if i not in n:
                    continue
                yacksoo.append(i)
                n.remove(i)
                m.remove(j)
    for i in yacksoo:
        baesoo.remove(i)
    for i in yacksoo:
        yackso *= int(i)
    for i in baesoo:
        baeso *= int(i)
    answer =[yackso,baeso]
    print(answer)
    return answer


def insoobunhae(n,m):
    nyacksoo=deque()
    myacksoo=deque()
    i=2
    while n!=1:
        if n%i==0:
            nyacksoo.append(i)
            n/=i
        else:
            i+=1
    i=2
    while m!=1:
        if m%i==0:
            myacksoo.append(i)
            m/=i
        else:
            i+=1
    return(nyacksoo,myacksoo)

n=228
m=81
solution(n,m)