import math
n = int(input())
num_array = list(map(int, input().split()))
dp = [0 for _ in range(n)]

dp[0] = num_array[0]
for index in range(1, len(num_array)):
    num = num_array[index]
    dp[index] = max(num, dp[index - 1] + num)

print(max(dp))