T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    for y in range(N):
        for x in range(N):
            tmp_max_count = 0
            for ny in range(M):
                for nx in range(M):
                    try:
                        tmp_max_count += graph[y + ny ][x + nx]
                    except:
                        continue
            max_count = max(max_count, tmp_max_count)

    print("#{} {}".format(i, max_count))