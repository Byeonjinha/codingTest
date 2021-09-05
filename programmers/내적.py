def solution(a, b):
    p=list(zip(a,b))
    for i in range(len(p)):
        p[i]=p[i][0]*p[i][1]
    return sum(p)

a= [1,2,3,4]
b=[-3,-1,0,2]
solution(a, b)