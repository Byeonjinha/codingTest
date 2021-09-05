from itertools import  combinations
def solution(num):
    if num==0:
        return 0
    insubunhae=[]
    k=[]
    gopaki=1
    i=2
    while num!=1:
        if num%i==0:
            insubunhae.append(i)
            num/=i
        else:
            i+=1
    for i2 in range(1,len(insubunhae)+1):
        p=list(set(combinations(insubunhae,i2)))
        for i3 in range(0,len(p)):
            for i4 in range(0, len(list(p[i3]))):
                gopaki*=list(p[i3])[i4]
            k.append(gopaki)
            gopaki=1
    return sum(k)+1
