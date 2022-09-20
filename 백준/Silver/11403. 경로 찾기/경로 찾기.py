from collections import defaultdict

N = int(input())
graph = []
nodeDic = defaultdict(list)
def check(index, nodeDic, visited):
    for i in nodeDic[index]:
        if visited[i] == 0:
            visited[i] = 1
            check(i, nodeDic, visited)
    return visited
for i in range(N):
    tmpGraph = list(map(int, input().split()))
    graph.append(tmpGraph)
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            nodeDic[i].append(j)
for i in range(N):
    visited = [0 for i in range(N)]

    for j in (check(i, nodeDic, visited)):
        print(j,end= " ")
    print()
