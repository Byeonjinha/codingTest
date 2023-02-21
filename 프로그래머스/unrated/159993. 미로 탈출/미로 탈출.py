from collections import deque
import copy
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def Lbfs(maps, y, x, move):
    global dx, dy
    maps[y][x] = move
    c = len(maps)
    r = len(maps[0])
    q = deque([])
    q.append((x,y,move))
    while q:
        x, y, count = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= r or nx < 0 or ny >= c or ny < 0:
                continue
            if maps[ny][nx] == "X":
                continue
            if isinstance(maps[ny][nx], int):
                maps[ny][nx] = min(maps[ny][nx], count + 1)
            else:
                q.append((nx, ny, count + 1))
                maps[ny][nx] = count + 1
                
def Ebfs(maps, y, x, move):
    global dx, dy
    maps[y][x] = move
    c = len(maps)
    r = len(maps[0])
    q = deque([])
    q.append((x,y,move))
    while q:
        x, y, count = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= r or nx < 0 or ny >= c or ny < 0:
                continue
            if maps[ny][nx] == "X":
                continue
            if isinstance(maps[ny][nx], int):
                maps[ny][nx] = min(maps[ny][nx], count + 1)
            else:
                q.append((nx, ny, count + 1))
                maps[ny][nx] = count + 1
                
def solution(maps):
    maps = list(map(list, maps))
    tmpMaps = copy.deepcopy(maps)
    S = (0,0)
    L = (0,0)
    E = (0,0)
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if maps[y][x] == "S":
                S = (y,x)
            if maps[y][x] == "L":
                L = (y,x)
            if maps[y][x] == "E":
                E = (y,x)

    Lbfs(tmpMaps, S[0], S[1], 0)

    if not isinstance(tmpMaps[L[0]][L[1]], int):
        return -1
    
    Ebfs(maps, L[0], L[1], tmpMaps[L[0]][L[1]])
    for i in maps:
        print(i)
    if not isinstance(maps[E[0]][E[1]], int):
        return -1
    for i in maps:
        print(i)
    return maps[E[0]][E[1]]