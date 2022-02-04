def solution(citations):
    dic = {}
    dic2 = {}
    for i in range(len(citations)):
        dic[citations[i]]=[0,0]
    for i in range(len(citations)):
        for j in dic:
            if j <= citations[i]:
                dic[j][0]+=1
            elif j > citations[i]:
                dic[j][1]+=1

    for j in dic:
        if j >= dic.get(j)[0] and j >= dic.get(j)[1]:
            dic2[j] = dic.get(j)
    if len(dic) ==1 :
        return 0

    answer = dic.get( min(dic2) )[0]
    return answer
citations = [0,0,0]
solution(citations)