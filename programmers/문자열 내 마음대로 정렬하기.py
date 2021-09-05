def solution(strings, n):
    strings2=[]
    answer=[]
    j=""
    for i in strings:
        i = list(i)
        strings2.append(tuple(i))

    for i in sorted(sorted(strings2), key=lambda x: x[n]):
        j= "".join(i)
        answer.append(j)
    return answer


strings = ["abce", "abcd", "cdx"]
n =2


solution(strings, n)