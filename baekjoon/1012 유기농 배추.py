import sys

sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False



T= int(sys.stdin.readline())


for i in range(T):
    result = 0
    n, m, j = map(int, input().split())
    graph =[[0 for _ in range(n)]for _ in range(m)]

    for i in range(j):
        x,y= map(int,input().split())
        graph[y][x]=1

    for i2 in range(m):
        for j2 in range(n):
            if dfs(i2,j2) ==True:
                result+=1
    print(result)

