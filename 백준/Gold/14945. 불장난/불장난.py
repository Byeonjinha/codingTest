def escape_lab(n):
    mod = 10007
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 초기값 설정
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 이동 가능한 방향은 아래 또는 오른쪽 아래 대각선
            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % mod
            dp[i][j] %= mod

    return dp[n][n]

# 입력 예제
n = int(input())

# 두 사람이 안전하게 방을 빠져나오는 경우의 수를 출력합니다.
print(escape_lab(n))
