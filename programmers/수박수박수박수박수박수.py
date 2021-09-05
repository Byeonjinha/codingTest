def solution(n):
    subak = []
    for i in range(1,n+1):
        if i%2==1:
            subak.append("수")
        else :
            subak.append("박")
    answer = "".join(subak)
    return answer