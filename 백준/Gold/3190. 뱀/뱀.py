import sys
from collections import deque
def tmpGraph(x,y,value):
    tmpMap = [[value for i in range(x)] for j in range(y)]
    return tmpMap
def move(funcDirection, moveCount, nextDirection, endCheck):
    global graph
    global snakeLocation
    global answer
    global nowLocation
    global nowDirection
    global cumulativetime
    global direction
    n = len(graph)
    moveCount -= cumulativetime
    cumulativetime += moveCount

    while moveCount != 0:
        answer += 1
        nextLocation = [nowLocation[0]+funcDirection[0],nowLocation[1]+funcDirection[1]]
        if nextLocation[0] < 0 or nextLocation[0] >= n or nextLocation[1] < 0 or nextLocation[1] >= n:
            print(answer)
            return False
        if graph[nextLocation[0]][nextLocation[1]] == "뱀":
            print(answer)
            return False
        if graph[nextLocation[0]][nextLocation[1]] == 1:
            snakeLocation.append(nextLocation)
            graph[nextLocation[0]][nextLocation[1]] = "뱀"
            nowLocation = nextLocation
        elif graph[nextLocation[0]][nextLocation[1]] == 0:
            previousLocation = snakeLocation.popleft()
            graph[previousLocation[0]][previousLocation[1]] = 0
            snakeLocation.append(nextLocation)
            graph[nextLocation[0]][nextLocation[1]] = "뱀"
            nowLocation = nextLocation
        moveCount -= 1
    if nextDirection == "L":
        nowDirection = (nowDirection+3) % 4
    elif nextDirection == "D":
        nowDirection = (nowDirection+1) % 4

    if endCheck:
        while True:
            funcDirection = direction[nowDirection]
            answer += 1
            nextLocation = [nowLocation[0] + funcDirection[0], nowLocation[1] + funcDirection[1]]
            if nextLocation[0] < 0 or nextLocation[0] >= n or nextLocation[1] < 0 or nextLocation[1] >= n:
                print(answer)
                return False
            if graph[nextLocation[0]][nextLocation[1]] == "뱀":
                print(answer)
                return False
            if graph[nextLocation[0]][nextLocation[1]] == 1:
                snakeLocation.append(nextLocation)
                graph[nextLocation[0]][nextLocation[1]] = "뱀"
                nowLocation = nextLocation
            elif graph[nextLocation[0]][nextLocation[1]] == 0:
                previousLocation = snakeLocation.popleft()
                graph[previousLocation[0]][previousLocation[1]] = 0
                snakeLocation.append(nextLocation)
                graph[nextLocation[0]][nextLocation[1]] = "뱀"
                nowLocation = nextLocation
    return True

boardSize = int(sys.stdin.readline())
graph = tmpGraph(boardSize, boardSize, 0)
cumulativetime = 0
appleCount = int(sys.stdin.readline())
nowLocation = [0,0]
snakeLocation = deque([[0,0]])
for i in range(appleCount):
    graph[nowLocation[0]][nowLocation[1]] = "뱀"
    appleLocation = list(map(int, input().split(' ')))
    graph[appleLocation[0]-1][appleLocation[1]-1] = 1

moveCount = int(sys.stdin.readline())
answer = 0
direction = [[0,1],[1,0],[0,-1],[-1,0]]
nowDirection = 0
endCheck = False
for j in range(moveCount):
    X, C = list(input().split(' '))
    if moveCount-1 == j:
        endCheck = True
    if not move(direction[nowDirection], int(X), C, endCheck):
        break
