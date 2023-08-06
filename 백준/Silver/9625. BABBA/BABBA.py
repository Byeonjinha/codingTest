dp = [[0, 0] for _ in range(47)]
for i in range(len(dp)):
    if i == 0:
        dp[i] = [1, 0]
    elif i == 1:
        dp[i] = [0, 1]
    else:
        dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]

num = int(input())
print(dp[num][0], dp[num][1])