from collections import deque
import  sys


def solution(board):
    n=len(board)
    m=len(board)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    bfs(0, 0,dx,dy,board,n,m)

def bfs(x,y,dx,dy,graph,n,m):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or ny<0 or nx >=n or ny>=m:
                continue
            if graph[nx][ny] ==1:
                continue
            if graph[nx][ny] ==0:

                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    print(graph[n-1][m-1])
    return graph[n-1][m-1]



board= [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
solution(board)
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
