import copy
import sys
from collections import deque
from collections import defaultdict
N, M = list(map(int, sys.stdin.readline().split()))
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
numList = [_ for _ in range(1,N+1)]
dx = [1, -1 , 0, 0]
dy = [0, 0, 1, -1]
answer = 0
def dropDown(graph):
    while True:
        tmpGraph = copy.deepcopy(graph)
        for y in range(len(graph)-1,0,-1):
            for x in range(len(graph[y])):
                if graph[y][x] == -1:
                    continue
                if graph[y-1][x] == -1:
                    continue
                if graph[y][x] == []:
                    graph[y][x], graph[y-1][x] = graph[y-1][x], graph[y][x]
        if graph == tmpGraph:
            return graph
def pang(graph,y,x):
    global dx,dy
    value = graph[y][x]
    graph[y][x] = []
    queue = deque()
    queue.append((y,x))
    while queue:
        y,x = queue.popleft()
        for direction in range(4):
            ny = y + dy[direction]
            nx = x + dx[direction]
            if ny >= N or ny < 0 or nx >= N or nx < 0:
                continue
            if graph[ny][nx] == value or graph[ny][nx] == 0:
                graph[ny][nx] = []
                queue.append((ny,nx))
    return graph
def pangCount(graph):
    global dx, dy, N, numList
    visited = [[False for _ in range(N)] for _ in range(N)]
    countList = []

    queue = deque()

    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x] == 0 :
                continue
            if graph[y][x] == -1 or graph[y][x] == []:
                visited[y][x] = True
            value = graph[y][x]
            count = 1
            rainbowCount = 0
            visitedLocation = []
            visitedLocation.append((y,x))
            if not visited[y][x]:
                queue.append((y,x))
                visited[y][x] = True
            while queue:
                y2, x2 = queue.popleft()
                for direction in range(4):
                    ny = y2 + dy[direction]
                    nx = x2 + dx[direction]
                    if ny >= N or ny < 0 or nx >= N or nx <0:
                        continue
                    if graph[ny][nx] == -1:
                        continue
                    if graph[ny][nx] in numList and graph[ny][nx] != value:
                        continue
                    if graph[ny][nx] == value:
                        if (ny,nx) not in visitedLocation:
                            visited[ny][nx] = True
                            visitedLocation.append((ny,nx))
                            count += 1
                            queue.append((ny,nx))
                    if graph[ny][nx] == 0 :
                        if (ny, nx) not in visitedLocation:
                            rainbowCount += 1
                            visitedLocation.append((ny,nx))
                            count += 1
                            queue.append((ny, nx))
            if count != 1 :
              countList.append([count, rainbowCount, y, x])
    countList.sort(key= lambda value : (-value[0], -value[1], -value[2], -value[3]) )
    if len(countList) == 0 :
        return False
    return countList[0]
def gravity(graph):
    for i in graph:
        print(i)
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
while True:
    pangSerch =  pangCount(graph)
    if not pangSerch:
        break
    answer += pangSerch[0] ** 2
    graph = pang(graph,pangSerch[2],pangSerch[3])

    graph = dropDown(graph)

    graph = rotate(graph,1,False)
    graph = dropDown(graph)

print(answer)

#
#
# graph = rotate(graph,1,False)
# for i in graph:
#     print(i)
