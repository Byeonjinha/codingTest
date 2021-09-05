def solution(s):
    s=list(s)
    if len(s)%2 ==0:
        return "".join(s[int(len(s)/2)-1:int(len(s)/2)+1])
    else :
        return "".join(s[int(len(s)/2)])
