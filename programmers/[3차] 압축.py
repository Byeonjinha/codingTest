from string import ascii_uppercase
from collections import deque
alpha = list(ascii_uppercase)
answer=[]
def ito(msg):
    temp = 0
    v=msg.popleft()
    while temp != 1:
        if v in alpha and len(msg)==0:
            answer.append(alpha.index(v) + 1)
            return

        if v in alpha:
            v+=msg.popleft()

        else:
            answer.append(alpha.index(v[:-1])+1)
            alpha.append(v)
            msg.appendleft(v[-1])
            temp+=1
    if 0== len(msg):
        return
    else:

        ito(msg)

def solution(msg):

    msg = deque(msg)
    ito(msg)
    return answer

msg	=  'ABABABABABABABAB'
solution(msg)