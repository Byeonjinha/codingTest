def vali(y,x,m,n):
    return 0 <= y < n and 0 <= x < m

def solution(m, n, puddles):
    graph = [[1 for _ in range(m)] for _ in range(n)]
    for y, x in puddles:
        graph[x - 1][y - 1] = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0 or (y == 0 and x == 0):
                continue
            else:
                a, b = 0, 0
                if vali(y, x - 1, m, n):
                    a = graph[y][x - 1]
                if vali(y - 1, x, m, n):
                    b = graph[y - 1][x]
                graph[y][x] = a + b
    return graph[y][x] % 1000000007