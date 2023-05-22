
dy, dx = [0,1,0,-1], [1,0,-1,0]
d = 0 
def validation(ny, nx, n):
    return 0 <= ny < n and 0 <= nx < n
def solution(n):
    global d, dy, dx
    current = [0, -1]
    answer = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n ** 2 + 1):
        y, x = current 
        ny = y + dy[d]
        nx = x + dx[d]
        if validation(ny, nx, n) and answer[ny][nx] == 0:
            answer[ny][nx] = i
        else:
            d = (d+1) % 4
            ny = y + dy[d]
            nx = x + dx[d]
            answer[ny][nx] = i
        current = [ny, nx]
    return answer