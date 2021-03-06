
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
from collections import deque

count = 0


def solution(board, c):
    n = len(board)
    m = len(board[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    point = []
    goal = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2:
                board[i][j]= 0
                point.append([i, j])
            if board[i][j] == 3:
                goal.append([i, j])
    answer = bfs(point[0][0], point[0][1], dx, dy, n, m, board,goal[0][0],goal[0][1])
    print(answer)
    return answer


def bfs(x, y, dx, dy, n, m, board,x2,y2):
    global count;\

    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == 0 or  board[nx][ny] == 3:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
            if board[nx][ny] == 1:
                continue
    for i in board:
        return board[x2][y2]