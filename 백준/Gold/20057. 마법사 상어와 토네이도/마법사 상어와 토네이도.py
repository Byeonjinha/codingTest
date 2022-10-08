import sys
import math
N = int(sys.stdin.readline())
graph = []
answer = 0

def westT(location):

    global graph , answer, N
    x, y = location[0], location[1]
    dusts = [0,0,0,0,0,0,0,0,0,0]
    dx = [0,-1,0,1,-2,-1,0,1,0,-1]
    dy = [-2,-1,-1,-1,0,1,1,1,2,0]
    for i in range(10):
        nx = x + dx[i]
        ny = y + dy[i]
        if i == 0 or i == 8:
            dust = math.floor(graph[y][x]  * 2 / 100)
            dusts[i] = dust
        elif i == 1 or i == 5:
            dust = math.floor(graph[y][x] * 10 / 100)
            dusts[i] = dust
        elif i == 2 or i == 6:
            dust = math.floor(graph[y][x] * 7 / 100)
            dusts[i] = dust
        elif i == 3 or i == 7:
            dust = math.floor(graph[y][x] * 1 / 100)
            dusts[i] = dust
        elif i == 4:
            dust = math.floor(graph[y][x] * 5 / 100)
            dusts[i] = dust
        elif i == 9:
            dust = graph[y][x] - sum(dusts)
        if nx >= N or nx <0 or ny >= N or ny <0: #넘어가면 정답에 먼지양을 더해줌
            answer += dust
            continue
        graph[ny][nx] += dust
    graph[y][x] = 0

def southT(location):
    global graph, answer, N
    x, y = location[0], location[1]
    dusts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dx = [-1, 1, -2, -1, 1, 2, -1, 1, 0, 0]
    dy = [-1, -1, 0, 0, 0, 0, 1, 1, 2, 1]
    for i in range(10):
        nx = x + dx[i]
        ny = y + dy[i]
        if i == 0 or i == 1:
            dust = math.floor(graph[y][x] * 1 / 100)
            dusts[i] = dust
        elif i == 2 or i == 5:
            dust = math.floor(graph[y][x] * 2 / 100)
            dusts[i] = dust
        elif i == 3 or i == 4:
            dust = math.floor(graph[y][x] * 7 / 100)
            dusts[i] = dust
        elif i == 6 or i == 7:
            dust = math.floor(graph[y][x] * 10 / 100)
            dusts[i] = dust
        elif i == 8:
            dust = math.floor(graph[y][x] * 5 / 100)
            dusts[i] = dust
        elif i == 9:
            dust = graph[y][x] - sum(dusts)
        if nx >= N or nx < 0 or ny >= N or ny < 0:  # 넘어가면 정답에 먼지양을 더해줌
            answer += dust
            continue
        graph[ny][nx] += dust
    graph[y][x] = 0
def eastT(location):
    global graph, answer, N
    x, y = location[0], location[1]
    dusts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dx = [0, -1, 0, 1, 2, -1, 0, 1, 0, 1]
    dy = [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0]
    for i in range(10):
        nx = x + dx[i]
        ny = y + dy[i]
        if i == 0 or i == 8:
            dust = math.floor(graph[y][x] * 2 / 100)
            dusts[i] = dust
        elif i == 1 or i == 5:
            dust = math.floor(graph[y][x] * 1 / 100)
            dusts[i] = dust
        elif i == 2 or i == 6:
            dust = math.floor(graph[y][x] * 7 / 100)
            dusts[i] = dust
        elif i == 3 or i == 7:
            dust = math.floor(graph[y][x] * 10 / 100)
            dusts[i] = dust
        elif i == 4:
            dust = math.floor(graph[y][x] * 5 / 100)
            dusts[i] = dust
        elif i == 9:
            dust = graph[y][x] - sum(dusts)
        if nx >= N or nx < 0 or ny >= N or ny < 0:  # 넘어가면 정답에 먼지양을 더해줌
            answer += dust
            continue
        graph[ny][nx] += dust
    graph[y][x] = 0
def northT(location):
    global graph, answer, N
    x, y = location[0], location[1]
    dusts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dx = [0, -1, 1, -2, -1, 1, 2, -1, 1, 0]
    dy = [-2, -1, -1, 0, 0, 0, 0, 1, 1, -1]
    for i in range(10):
        nx = x + dx[i]
        ny = y + dy[i]
        if i == 0:
            dust = math.floor(graph[y][x] * 5 / 100)
            dusts[i] = dust
        elif i == 1 or i == 2:
            dust = math.floor(graph[y][x] * 10 / 100)
            dusts[i] = dust
        elif i == 3 or i == 6:
            dust = math.floor(graph[y][x] * 2 / 100)
            dusts[i] = dust
        elif i == 4 or i == 5:
            dust = math.floor(graph[y][x] * 7 / 100)
            dusts[i] = dust
        elif i == 7 or i == 8:
            dust = math.floor(graph[y][x] * 1 / 100)
            dusts[i] = dust
        elif i == 9:
            dust = graph[y][x] - sum(dusts)
        if nx >= N or nx < 0 or ny >= N or ny < 0:  # 넘어가면 정답에 먼지양을 더해줌
            answer += dust
            continue
        graph[ny][nx] += dust
    graph[y][x] = 0


for i in range(N):
     graph.append(list(map(int,sys.stdin.readline().split())))
location = [N//2 , N//2]
direction = 0
west = N//2
south = N//2
east = N//2
north = N//2
while location != [-1,0]:
    if direction%4 == 0:
        west -= 1
        while location != [west, north]:
            location[0] -= 1
            westT(location)


        direction += 1
    elif direction%4 == 1:
        south += 1
        while location != [west, south]:
            location[1] += 1
            southT(location)


        direction +=1
    elif direction%4 == 2:
        east += 1
        while location != [east, south]:
            location[0] += 1
            eastT(location)


        direction +=1
    elif direction%4 == 3:
        north -= 1
        while location != [east, north]:
            location[1] -= 1
            northT(location)


        direction +=1

print(answer)