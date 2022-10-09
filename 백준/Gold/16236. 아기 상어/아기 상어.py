import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
levelUpExp = 2
exp = 0
sharkSize = 2
location = [0,0]
time = 0
# distance, y, x 순으로 담아줌
def fishCheck(location):
    global graph, N, sharkSize
    graph[location[1]][location[0]] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    canEatFish = []
    movedLocation = deque()
    movedLocation.append(tuple(location))
    visited = []
    while movedLocation:
        x,y, moveCount = movedLocation.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if graph[ny][nx] > sharkSize:
                continue
            if graph[ny][nx] == sharkSize or graph[ny][nx] == 0 :
                if (nx, ny) not in visited:
                    visited.append((nx,ny))
                    movedLocation.append((nx, ny, moveCount+1))
            if graph[ny][nx] < sharkSize:
                if (nx,ny) not in visited:
                    visited.append((nx, ny))
                    canEatFish.append([moveCount,ny,nx])
    canEatFish.sort(key = lambda x: (x[0],x[1],x[2]))
    if len(canEatFish) ==0 :
        return False
    return canEatFish[0] #distance , y좌표 , x 좌표 리턴
def levelUpCheck():
    global exp, levelUpExp, sharkSize
    exp += 1
    if exp == levelUpExp:
        sharkSize += 1
        levelUpExp = sharkSize
        exp = 0
for y in range(len(graph)):
    for x in range(len(graph[y])):
        if graph[y][x] == 9:
            location = [x,y,1]

while True:
    targetFish = fishCheck(location)
    if not targetFish:
        break
    time += targetFish[0]
    y = targetFish[1]
    x = targetFish[2]
    graph[y][x] = 0
    location = [x,y,1]
    levelUpCheck()
print(time)