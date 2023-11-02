from collections import deque
import  copy
r, c, k = map(int, input().split())
graph = [list(input()) for _ in range(r)]
roads = []

def isValid(y, x):
    global r, c
    return 0 <= y < r and 0 <= x < c

def bfs():
    global graph, r, c, k, roads
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([])
    visited_graph = [[False for _ in range(len(graph[y]))] for y in range(len(graph))]
    visited_graph[r - 1][0] = True
    q.append((r - 1, 0, visited_graph, [[r - 1, 0]]))

    while q:
        y, x, visited_graph, road = q.popleft()
        for d in range(4):
            tmp_graph = copy.deepcopy(visited_graph)
            ny = y + dy[d]
            nx = x + dx[d]

            if ny == 0 and nx == c - 1 and len(road) == k - 1 and not tmp_graph[ny][nx]:
                if road not in roads:
                    roads.append(road)
                continue


            if isValid(ny, nx) and not tmp_graph[ny][nx] and graph[ny][nx] != "T":
                tmp_graph[ny][nx] = True
                q.append((ny, nx, tmp_graph, road + [[ny, nx]]))


bfs()
print(len(roads))