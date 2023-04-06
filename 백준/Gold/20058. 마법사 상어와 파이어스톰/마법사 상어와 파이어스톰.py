import copy
import sys
from collections import deque
def rotate(graph, count, direction):

    N = len(graph)
    M = len(graph[0])
    if not direction:
        count += 2
    if count%2 == 1:
        ret = [[0] * N for _ in range(M)]
    else:
        ret = [[0] * M for _ in range(N)]
    if count%4 == 1:
        for r in range(N):
            for c in range(M):
                ret[c][N - 1 - r] = graph[r][c]
        return ret
    elif count%4 == 2:
        for r in range(N):
            for c in range(M):
                ret[N - 1 - r][(M-1) - c] = graph[r][c]

        return ret
    elif count%4 == 3:
        for r in range(N):
            for c in range(M):
                ret[M- 1 -c][r] = graph[r][c]
        return ret
    else:
        return graph
    return graph
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def ice():
    global dx,dy, graph, N
    visited = copy.deepcopy(graph)
    queue = deque()
    tmpList = []
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x] == 0:
                continue
            iceCount = 0
            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if nx >= 2**N or nx < 0 or ny >= 2**N or ny<0:
                    continue
                if graph[ny][nx] != 0:
                    iceCount += 1
            if 3 > iceCount:
                tmpList.append((y,x))
    for i in range(len(tmpList)):
        deleteX = tmpList[i][1]
        deleteY = tmpList[i][0]
        graph[deleteY][deleteX] -= 1
def iceCount():
    global dx,dy, graph, N
    visited = copy.deepcopy(graph)
    queue = deque()
    tmpList = []
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x] == 0:
                visited[y][x] = False
            if visited[y][x]:
                visitedXY = []
                visitedXY.append((y,x))
                queue.append((y,x))
                iceCount = 1
                while queue:
                    y, x = queue.popleft()
                    visited[y][x] = False
                    for direction in range(4):
                        nx = x + dx[direction]
                        ny = y + dy[direction]
                        if nx >= 2**N or nx < 0 or ny >= 2**N or ny<0 :
                            continue
                        if graph[ny][nx] == 0:
                            continue
                        if graph[ny][nx] != 0:
                            visited[y][x] = False
                            if (ny,nx) not in visitedXY:
                                queue.append((ny,nx))
                                visitedXY.append((ny,nx))
                                iceCount += 1
                tmpList.append(iceCount)
    if len(tmpList) == 0:
        return 0
    return max(tmpList)

N,Q = list(map(int,sys.stdin.readline().split()))
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(2**N)]
magicList = list(map(int,sys.stdin.readline().split()))

for magic in magicList:
    if magic != 0:
        for magicLength in range(2**(N-magic)):
            for magicLength2 in range(2 ** (N - magic)):
                tmpGraph = [[0 for _ in range(2**magic)] for _ in range(2**magic)]
                for tmpY in range(2**magic):
                    for tmpX in range(2**magic):
                        y = tmpY + 2 ** magic * magicLength
                        x = tmpX + 2 ** magic * magicLength2
                        tmpGraph[tmpY][tmpX] = graph[y][x]
                tmpGraph = rotate(tmpGraph,1,True)

                for tmpY in range(2 ** magic):
                    for tmpX in range(2 ** magic):
                        y = tmpY + 2 ** magic * magicLength
                        x = tmpX + 2 ** magic * magicLength2
                        graph[y][x] = tmpGraph[tmpY][tmpX]
        ice()
    if magic ==0:
        ice()
count = iceCount()
answer = 0
for ices in graph:
    answer += sum(ices)
print(answer)
print(count)