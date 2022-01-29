cheyookbok=[]
def solution(n, lost, reserve):
    for i in range(n):
        cheyookbok.append(1)
    cheyookboklost(lost)
    cheyookbokreserve(reserve)
    for i in range(n-1):
        if cheyookbok[i]==0 and cheyookbok[i+1]==2:
            cheyookbok[i]+=1
            cheyookbok[i+1]-=1
        elif cheyookbok[i]==2 and cheyookbok[i+1]==0:
            cheyookbok[i]-=1
            cheyookbok[i+1]+=1
    if cheyookbok[-2]==0 and cheyookbok[-1]==2:
        cheyookbok[-2]+=1
        cheyookbok[-1]-=1
    elif cheyookbok[-1]==2 and cheyookbok[-2]==0:
        cheyookbok[-2]-=1
        cheyookbok[-1]+=1
    print(cheyookbok)
    answer = n-cheyookbok.count(0)
    return answer


def cheyookboklost(lost):
    for i in lost:
        cheyookbok[i-1]-=1
    print(cheyookbok)

def cheyookbokreserve(reserve):
    for i in reserve:
        cheyookbok[i-1]+=1

n=10
lost=[2, 4,10]
reserve=[1, 3, 5,9]
solution(n, lost, reserve)