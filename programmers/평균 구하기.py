def solution(x):
    sum=0
    x=str(x)
    for i in x:
        sum+=int(i)
    if int(x)%sum==0:
        answer = True
    else :
        answer = False
    return answer
