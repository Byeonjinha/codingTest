from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(sx, sy, ax, ay,s):
    q = deque()
    q.append([sx, sy])
    s[sx][sy] = 1
    while q:
        a, b = q.popleft()
        if a == ax and b == ay:
            print(s[ax][ay] -1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0:
                q.append([x, y])
                s[x][y] = s[a][b] + 1
def chess(n,chulbal,dochack):
    sx, sy = chulbal
    ax, ay = dochack
    s = [[0] * n for i in range(n)]
    bfs(sx, sy, ax, ay,s)


n=100
chulbal= [0,0]
dochack= [30,50]
chess(n,chulbal,dochack)




# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1