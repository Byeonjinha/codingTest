a= int(input())
dp = [0 for _ in range(a+4)]
dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=3
for i in range(4, a + 1):
    dp[i] = dp[i - 1] + dp[i-2]
print(dp[a]%10007)
