import sys
from collections import defaultdict
N, M, y, x, command_count = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
command = list(map(int, sys.stdin.readline().strip().split()))
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

dice = defaultdict(int)

for i in range(1, 7):
    dice[i] = 0

def check(direction):
    global x, y, dx, dy
    nx = x + dx[direction - 1]
    ny = y + dy[direction - 1]
    if ny >= N or ny < 0 or nx >= M or nx < 0:
        return False
    x, y = nx, ny
    return True

def move_dice(graph, direction):
    global dice, x, y

    if direction == 1:
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    elif direction == 2:
        dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]
    elif direction == 3:
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]
    elif direction == 4:
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
    if graph[y][x] == 0:
        graph[y][x] = dice[1]
    else:
        dice[1], graph[y][x] = graph[y][x], 0

    print(dice[6])

# dice[1] = graph[y][x]
for direction in command:
    if check(direction):
        move_dice(graph, direction)