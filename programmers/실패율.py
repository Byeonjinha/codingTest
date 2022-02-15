def solution(N, stages):
    dic = {}
    list_1 = []
    for i in range(len(stages)):
        if stages[i] not in dic:
            dic[stages[i]]=1
        else:
            dic[stages[i]]+=1
    boonmo=0
    for i in range(1,N+1):
        for j in dic:
            if i<= j :
                boonmo+= dic.get(j)
        boonja = dic.get(i)
        if boonja is None:
            boonja=0
        if boonmo==0:
            list_1.append([i,0])
        else:
          list_1.append([i,boonja/boonmo])
        boonmo=0
    answer = []
    list_1.sort(key=lambda x : (-x[1], x[0]))
    for i in range(len(list_1)):
        answer.append(list_1[i][0])

    print(answer)
    return answer
N = 4
stages = [4,4,4,4,4]
solution(N, stages)