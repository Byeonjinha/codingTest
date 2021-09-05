from collections import deque
import  sys

n,m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or ny<0 or nx >=n or ny>=m:
                continue
            if graph[nx][ny] ==0:
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))
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
