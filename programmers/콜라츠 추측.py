def solution(num):
    count=0
    while num!=1:
        if num%2==0:
            count+=1
            num/=2
            if count==500:
                break
        else:
            count+=1
            num=num*3+1
            if count==500:
                break
    if count ==500:
        answer = -1
    else:
        answer =count
    return answer
