import copy
# N= 4
# stages=	[4,4,4,4,4]
# N= 5
# stages=	[2, 1, 2, 6, 2, 4, 3, 3]
# N= 6
# stages=	[1, 1, 1, 1, 2, 2, 2, 2]


silpae=[]
silpae2=[]


def solution(N, stages):
    clear = [0 for _ in range(N + 1)]
    answer =[]
    for i in stages:
        clear[i-1]+=1
    for i  in range(0,len(clear)-1):
        if sum(clear[i::])==0:
            silpae.append(0)
        else:
            silpae.append(clear[i]/sum(clear[i::]))

    # if max(stages)-N== 1:
    #     del silpae[-1]
    silpae2 = copy.deepcopy(silpae)
    silpae2.sort(reverse=True)
    for i in silpae2:
        answer.append(silpae.index(i)+1)
        silpae[silpae.index(i)]=''
    print(answer)
    return answer
solution(N, stages)




