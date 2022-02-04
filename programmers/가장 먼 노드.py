import math
def solution(n, edge):
    dist = [math.inf for i in range(n+1)]

    temp = []
    temp2= []

    for i in range(len(edge)):
        edge[i].sort()
        temp.append([edge[i],0])
    temp.sort(key=lambda x: (x[0],x[1]))
    for j in range(len(temp)):

        if temp[j][0][0]==1:
            temp2.append(temp[j])

        while temp2:
            x= temp2.pop()
            x[1] += 1
            if dist[x[0][1]] >=  x[1] :
                dist[x[0][1]]=x[1]
            for j in range(len(temp)):
                if temp[j][0][0] ==x[0][1]:
                    temp2.append([temp[j][0],temp[j][1]+1])
    dist[0],dist[1]=-1,-1
    print(dist)
    answer = dist.count(max(dist))
    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n,vertex)