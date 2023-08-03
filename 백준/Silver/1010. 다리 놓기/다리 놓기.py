def bridge(left, right):
    DP = [[i + 1 for i in range(right)] for _ in range(left)]

    for l in range(left):
        for r in range(l, right):
            if l == 0: continue
            if l == r:
                DP[l][r] = 1
            else:
                DP[l][r] = DP[l][r - 1] + DP[l - 1][r - 1]
    return DP[-1][-1]

t = int(input())

for _ in range(t):
    left, right = map(int, input().split())

    print(bridge(left, right))