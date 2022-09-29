import copy
import sys
from collections import deque
import copy
graphLength = int(sys.stdin.readline())
graph = []
graph2 = []
count = 1
count2 = 1
rgb = ["R","G","B","RG"]
answer = []
def bfs(graph, x, y):
    global count
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    now = graph[x][y]
    n = len(graph)
    m = len(graph[0])
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if graph[nx][ny] == now:
                graph[nx][ny] = count
                queue.append((nx,ny))
    count += 1

for i in range(graphLength):
    pieceGraph = list(sys.stdin.readline().strip())
    graph.append(copy.deepcopy(pieceGraph))
    for j in range(len(pieceGraph)):
        if pieceGraph[j] == "R" or pieceGraph[j] == "G":
            pieceGraph[j] = "RG"
    graph2.append(pieceGraph)
for j in range(len(graph)):
    for j2 in range(len(graph[j])):
        if graph[j][j2] in rgb:
            bfs(graph,j,j2)
answer.append(str(count-1))
count = 1
for j in range(len(graph2)):
    for j2 in range(len(graph2[j])):
        if graph2[j][j2] in rgb:
            bfs(graph2,j,j2)
answer.append(str(count-1))
print(" ".join(answer))

