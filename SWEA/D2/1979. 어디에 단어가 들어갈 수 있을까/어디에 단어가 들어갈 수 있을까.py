# 10
# 5 3
# 0 0 1 1 1
# 1 1 1 1 0
# 0 0 1 0 0
# 0 1 1 1 1
# 1 1 1 0 1

T = int(input())
for i in range(1, T + 1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for y in range(N):
        count = 0
        for x in range(N):
            if graph[y][x] == 1:
                count += 1
            else:
                if count == K:
                    answer += 1
                count = 0
        if count == K:
            answer += 1
    graph = list(map(list, zip(*graph)))
    for y in range(N):
        count = 0
        for x in range(N):
            if graph[y][x] == 1:
                count += 1
            else:
                if count == K:
                    answer += 1
                count = 0
        if count == K:
            answer += 1
    print("#{} {}".format(i, answer))