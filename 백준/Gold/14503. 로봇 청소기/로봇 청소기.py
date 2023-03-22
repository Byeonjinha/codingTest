import sys

sys.setrecursionlimit(10 ** 4)
n, m = map(int, sys.stdin.readline().strip().split())
y, x, d = map(int, sys.stdin.readline().strip().split())
graphs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

answer = 0
dx, dy = [0 ,1 ,0, -1], [-1, 0, 1, 0]
# 북 동 남 서
def check():
    global x, y, dx, dy, d, graphs, n, m
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= m or nx < 0 or ny >= n or ny < 0:
            continue
        if graphs[ny][nx] == 1:
            continue
        if graphs[ny][nx] == 0:
            return False
    return True

def move():
    global x, y, graphs, d, dx, dy
    x = x + dx[d]
    y = y + dy[d]

def current_place_clear():
    global x, y, graphs, answer
    graphs[y][x] = "clear"
    answer += 1
    return

def move_back():
    global x, y, dx, dy, d
    x =  x + dx[(d + 2) % 4]
    y = y + dy[(d + 2) % 4]
    return

def back_check(): #뒤 확인 후 갈 곳이 벽이면 종료.
    global d, dx, dy, graphs
    nx = x + dx[(d + 2) % 4]
    ny = y + dy[(d + 2) % 4]
    if nx >= m or nx < 0 or ny >= n or ny < 0:
        return False
    if graphs[ny][nx] == 1:
        return True
    return False

def trans90():
    global d
    d = (d + 3) % 4

def check_front():
    global d, dx, dy, graphs
    nx = x + dx[d]
    ny = y + dy[d]
    if nx >= m or nx < 0 or ny >= n or ny < 0:
        return False
    if graphs[ny][nx] == 1:
        return False
    if graphs[ny][nx] == "clear":
        return False
    return True


while True:
    if graphs[y][x] == 0:
        current_place_clear()
    if check():
        if back_check():
            break
        else:
            move_back()
            continue
    else:
        while True:
            trans90()
            if check_front():
                break
        move()

print(answer)

