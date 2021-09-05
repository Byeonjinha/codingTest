import copy


def solution(s):
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    answer=[]
    a=s.split("{")
    b=''.join(a)
    c=b.split("}")
    while c.count("")!=0:
        c.remove("")
    for i in range(len(c)):
        p=c[i].split(',')
        while p.count("")!=0:
            p.remove("")
        for i2 in range(len(p)):
            q=int(p[i2])
            list1.append(q)
            list4.append(q)
        list2.append(copy.deepcopy(list1))
        list3.append(len(list1))
        list1.clear()

    max1 = list3.index(max(list3))
    for i in range(len(list2[max1])):
        list5.append([list2[max1][i] , list4.count(list2[max1][i])     ])

    list5.sort(key=lambda x:(-x[1],x[0]))
    for i in range(len(list5)):
        answer.append(list5[i][0])

    return answer



s="{{4,2,3},{3},{2,3,4,1},{2,3}}"

solution(s)