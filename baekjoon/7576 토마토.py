from collections import deque
import  sys
n,m = map(int, sys.stdin.readline().split())
graph = []
for i in range(m):
    graph.append(list(map(int,input().split())))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
def bfs(graph):
    k = 0
    queue=deque()
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j]==1:
                queue.append((i,j))

    while queue:
        k += 1
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or ny<0 or nx >=m or ny>=n:
                continue
            if graph[nx][ny] ==1:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] ==0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1
    return graph
answer = 0
for i in bfs(graph):
    if answer<max(i):
        answer=max(i)
    if 0 in i :
        print(-1)
        break
else:
    print(answer-1)


'''
10 10
1111111111
1000000001
1110000111
1100000101
1111011101
0010110101
0010110000
1110111111
1110111111
0000000001
'''
