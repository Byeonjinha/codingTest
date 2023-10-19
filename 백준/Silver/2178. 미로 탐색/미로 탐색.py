import math
from collections import deque

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = map(int, input().split())

sy, sx = 0, 0

graph = [list(map(int, list(input()))) for _ in range(n)]

accumulated_graph = [[math.inf for _ in range(m)] for _ in range(n)]

visited_graph = [[False for _ in range(m)] for _ in range(n)]

accumulated_graph[sy][sx], visited_graph[sy][sx] = 1, True

def validate(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs(y, x):
    global graph, accumulated_graph

    q = deque([])
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if validate(ny, nx) and graph[ny][nx] != 0 and not visited_graph[ny][nx]:
                accumulated_graph[ny][nx] = min(accumulated_graph[ny][nx], accumulated_graph[y][x] + 1)
                visited_graph[ny][nx] = True
                q.append((ny, nx))
bfs(sy, sx)

print(accumulated_graph[n - 1][m - 1])