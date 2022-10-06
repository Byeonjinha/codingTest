import copy


def cloudLocation(direction, count):
    global cloud
    tmpCLoud = []
    for i in cloud:
        if direction == 1:
            x = ((i[1] + N * 50) - count) % N
            y = i[0]
        elif direction ==2:
            x = ((i[1] + N * 50) - count) % N
            y = ((i[0] + N * 50) - count) % N
        elif direction ==3:
            x = i[1]
            y = ((i[0] + N * 50) - count) % N
        elif direction ==4:
            x = ((i[1] + N * 50) + count) % N
            y = ((i[0] + N * 50) - count) % N
        elif direction ==5:
            x = ((i[1] + N * 50) + count) % N
            y = i[0]
        elif direction ==6:
            x = ((i[1] + N * 50) + count) % N
            y = ((i[0] + N * 50) + count) % N
        elif direction ==7:
            x = i[1]
            y = ((i[0] + N * 50) + count) % N
        elif direction ==8:
            x = ((i[1] + N * 50) - count) % N
            y = ((i[0] + N * 50) + count) % N
        tmpCLoud.append((y,x))
    cloud = tmpCLoud

def addWater(cloud):
    global graph
    for x,y in cloud:
        graph[x][y] += 1

def waterCopy(cloud):
    global graph
    global N
    dx = [1, 1, -1, -1]
    dy = [-1, 1, 1, -1]
    for x,y in cloud:
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0 :
                continue
            if graph[nx][ny] == 0 :
                continue
            count += 1
        graph[x][y] += count

def newCloud():
    tmpCloud = []
    global graph
    global cloud
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] >= 2 and (i,j) not in cloud:
                tmpCloud.append((i,j))
                graph[i][j] -= 2
    cloud = tmpCloud
N, M = map(int,input().split())
graph = []
moves = []
for i in range(N):
    pieceGraph = list(map(int,input().split()))
    graph.append(pieceGraph)
for j in range(M):
    move = list(map(int,input().split()))
    moves.append(move)
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

for direction, count in moves:
    cloudLocation(direction, count)
    addWater(cloud)
    waterCopy(cloud)
    newCloud()
answer = 0
for i in graph:
    answer += sum(i)
print(answer)
