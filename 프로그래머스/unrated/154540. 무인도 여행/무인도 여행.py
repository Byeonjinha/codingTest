from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = []
def bfs(maps, n , m, x, y):
    global dx, dy, answer 
    value = int(maps[y][x])
    maps[y][x] = "X"
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny >= m or ny < 0 or nx >= n or nx < 0 or maps[ny][nx] == "X":
                continue
            q.append((nx,ny))
            value += int(maps[ny][nx])
            maps[ny][nx] = "X"
    return value
   
def solution(maps):    
    global answer
    n = len(maps[0])
    m = len(maps)
    graph = list(map(list,maps))
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if graph[y][x] != "X":
                answer.append(bfs(graph, n , m, x, y))
    answer.sort()
    if len(answer) == 0 :
        return [-1]
    return answer