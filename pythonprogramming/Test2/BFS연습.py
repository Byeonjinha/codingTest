def gippi(gujo,v,visited):
    visited[v]=True
    print(v,end=" ")
    for i in gujo[v]:
        if not visited[i]:
            gippi(gujo,i,visited)

gujo = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
print(visited)
gippi(gujo,7,visited)