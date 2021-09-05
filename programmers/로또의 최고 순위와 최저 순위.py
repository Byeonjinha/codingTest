answer=[]
def dangchum(deonsu):
    if len(deonsu)==6:
        answer.append(1)
    elif len(deonsu)==5:
        answer.append(2)
    elif len(deonsu)==4:
        answer.append(3)
    elif len(deonsu)==3:
        answer.append(4)
    elif len(deonsu)==2:
        answer.append(5)
    else:
        answer.append(6)
def solution(lottos, win_nums):
    deongsu = []
    lottos.sort()
    win_nums.sort()
    for i in lottos:
        if i==0:
            deongsu.append(i)
        for j in win_nums:
            if i == j:
                deongsu.append(i)
    dangchum(deongsu)

    while deongsu.count(0)!=0:
        deongsu.remove(0)
    dangchum(deongsu)
    return answer



