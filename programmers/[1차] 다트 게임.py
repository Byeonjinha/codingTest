def solution(dartResult):
    answer=[]
    for i in range(0,len(dartResult)-1):
        if dartResult[i] =='1' and  dartResult[i+1] =='0':
            answer.append("+")
            answer.append("10")
        elif dartResult[i] =='0' and  dartResult[i-1] =='1':
            continue
        elif dartResult[i] in ["0","1","2","3","4","5","6","7","8","9"]:
            answer.append("+")
            answer.append(dartResult[i])
        elif dartResult[i] =='*' and (i==2 or i==3):
            answer.append('*2')
        elif dartResult[i] =='*' and i!=2 and i!=3:
            v1=answer.pop()
            v2=answer.pop()
            v3=answer.pop()
            answer.append('*2')
            answer.append(v3)
            answer.append(v2)
            answer.append(v1)
            answer.append('*2')
        elif dartResult[i] =='#':
            answer.append('*(-1)')
        elif dartResult[i] =='S':
            answer.append('**1')
        elif dartResult[i] =='D':
            answer.append('**2')
        elif dartResult[i] =='T':
            answer.append('**3')
    if dartResult[-1] =='*':
        v1=answer.pop()
        v2=answer.pop()
        v3=answer.pop()
        answer.append('*2')
        answer.append(v3)
        answer.append(v2)
        answer.append(v1)
        answer.append('*2')
    elif dartResult[-1] =='#':
        answer.append('*(-1)')
    elif dartResult[-1] =='S':
        answer.append('**1')
    elif dartResult[-1] =='D':
        answer.append('**2')
    elif dartResult[-1] =='T':
        answer.append('**3')

    answer=''.join(answer)


    return eval(answer)

dartResult	= '0S1D2S3T*'
solution(dartResult)