import copy
import sys

N,M,k = list(map(int,sys.stdin.readline().split()))
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
shark = [[] for _ in range(M)]
# 샤크의 구성 =

def moveShark(tmpGraph):
    global shark, graph, dy, dx, N
    moveSharkList = []
    for y in range(len(tmpGraph)):
        for x in range(len(tmpGraph[y])):
            if len(tmpGraph[y][x]) != 0:
                if tmpGraph[y][x][0][0]: # 상어가 있는 상태라면
                    location =[y,x]  #위치확인을 하고
                    sharkNum = tmpGraph[y][x][0][1]-1
                    currentDirection =  tmpGraph[y][x][0][2]
                    nextDirections = shark[sharkNum][1][currentDirection]  # 상어의 이동순서배열을 불러옴
                    next = 0
                    directionCount = 4
                    while True:
                        nextDirection = nextDirections[next % 4] - 1
                        ny = y + dy[nextDirection]           #상어의 다음위치
                        nx = x + dx[nextDirection]
                        if nx >= N or nx < 0 or ny >= N or ny < 0: #범위를 넘어가면 다음 움직임
                            next += 1
                            directionCount -= 1
                            continue
                        if len(tmpGraph[ny][nx]) != 0: #다음칸에 무언가가 있고
                            if tmpGraph[ny][nx][0][1] != sharkNum+1: #그 냄새가 자신의 것이 아니라면
                                directionCount -= 1
                                next += 1 #회전
                                continue
                            elif tmpGraph[ny][nx][0][1] == sharkNum+ 1: # 그 냄새가 자신의 것이면
                                if directionCount > 0 : #한바퀴를 아직 돌아보지 않았다면
                                    next += 1 #좀더 돌아보라고 시킴
                                    directionCount -= 1
                                    continue
                                else:
                                    moveSharkList.append((y,x,ny,nx,sharkNum+1, nextDirection)) #
                                    #한바퀴 이상 돌아보고 자신의 냄새 있는 곳으로 밖에 가지 못할 때
                                    # 그 좌표, 상어 숫자, 상어방향을 araay에 담아주고 break
                                    break

                        if len(tmpGraph[ny][nx]) == 0 : # 다음 칸에 아무 것도 없을 때
                            moveSharkList.append((y,x,ny, nx, sharkNum+1, nextDirection))
                            break # 임시브레이크

    return moveSharkList
sharkDirection =  list(map(int,sys.stdin.readline().split()))
for originDirection in range(len(shark)):
    shark[originDirection].append(sharkDirection[originDirection])
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for sharkNum in range(len(shark)):
    sharkOriginDirections = []
    for inputDirection in range(4):
        sharkOriginDirections.append(list(map(int ,sys.stdin.readline().split())))
    shark[sharkNum].append(sharkOriginDirections)
for y in range(len(graph)):
    for x in range(len(graph[y])):
        if graph[y][x] == 0 :
            # graph[y][x] = [[False, 0,0,0]] # 냄새인지 진짜상어인지 구분하는 True , 상어숫자, 바라보는 방향, 상어냄새유지기간
            graph[y][x] = []
        else:
            graph[y][x] = [[True, graph[y][x], shark[ graph[y][x]-1][0]-1, k]]
sharkCount = M
time = 0
while sharkCount != 1:
    sharkCount = 0
    time += 1
    if time > 1000:
        break
    moveSharks = moveShark(graph)
    for y,x,ny,nx, num, d in moveSharks:
        graph[y][x][0][0] = False #상어가 없다고 표시
        graph[ny][nx].append([True,num,d,k]) #상어 데이터를를 append
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if len(graph[y][x]) == 1: #무언가가 한개 들어있는 상황
                if not graph[y][x][0][0]: #냄새만있을때
                    graph[y][x][0][3] -= 1
                if graph[y][x][0][3] == 0:
                    graph[y][x].pop()
            elif len(graph[y][x]) >= 2:
                graph[y][x].sort(key = lambda x: (x[1],-x[3]))
                while len(graph[y][x]) != 1:
                    a = graph[y][x].pop()
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if len(graph[y][x]) != 0 :
                if graph[y][x][0][0]:
                    sharkCount += 1
if time > 1000:
    print(-1)
else:
    print(time)