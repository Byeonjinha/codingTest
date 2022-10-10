import copy
import sys
from collections import defaultdict
N = int(sys.stdin.readline())
dx = [1, -1 , 0, 0]
dy = [0, 0, 1, -1]
students = [list(map(int,sys.stdin.readline().split())) for _ in range(N**2)]
graph = [[0 for _ in range(N)] for _ in range(N)]
def checkManjoke(y,x,student ,graph):
    global dx,dy,N, studentsDic
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>= N or nx < 0 or ny >= N or ny <0 :
            continue
        if graph[ny][nx] in studentsDic[student]:
            count += 1
    if count == 0:
        return 0
    elif count == 1:
        return 1
    elif count == 2:
        return 10
    elif count == 3:
        return 100
    elif count == 4:
        return 1000
def checkStudent(graph,location,num):
    global students, dx ,dy, N, studentsDic
    x, y = location
    count = 0
    empty = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>= N or nx < 0 or ny >= N or ny <0 :
            continue
        if graph[nx][ny] in studentsDic[num]:
            count += 1
        if graph[nx][ny] == 0 :
            empty += 1
    return [count, empty, y, x]
locations = []
studentsDic = defaultdict(list)
for i in range(len(students)):
    for j in range(len(students[i])):
        if j != 0 :
            studentsDic[students[i][0]].append(students[i][j])
answer = 0
for studentNum in range(len(students)):
    locationList = []

    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x] == 0:
                location = (y,x)
                locationList.append(checkStudent(graph,location,students[studentNum][0]))
    locationList.sort(key = lambda x: (-x[0],-x[1],x[3],x[2]))
    newY = locationList[0][3]
    newX = locationList[0][2]
    graph[newY][newX] = students[studentNum][0]
for i in range(len(graph)):
    for j in range(len(graph[i])):
        answer += checkManjoke(i,j,graph[i][j],graph)
print(answer)