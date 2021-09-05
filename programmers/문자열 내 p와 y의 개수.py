def solution(s):
    p=s.upper()
    pcount = 0
    ycount = 0
    for i in p:
        if i =="P":
            pcount+=1
        if i =="Y":
            ycount+=1
    if pcount==ycount:
        return True
    return False

s="pPoooyY"
solution(s)