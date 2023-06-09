T = int(input())

for t in range(1, T + 1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]

    num = 1
    y, x = 0, -1
    d = 0
    move = N * N
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]


    def validations(ny, nx):
        global N, snail
        if 0 <= ny < N and 0 <= nx < N:
            if snail[ny][nx] == 0:
                return True
            return False


    for _ in range(move):
        while True:
            ny = y + dy[d]
            nx = x + dx[d]
            if validations(ny, nx):
                snail[ny][nx] = num
                num += 1
                y, x = ny, nx
                break
            else:
                d = (d + 1) % 4

    # 달팽이 출력
    print("#{}".format(t))
    for row in snail:
        print(*row)
