import sys
import math
input = sys.stdin.readline
t = int(input())
dp = [[math.inf for _ in range(3)] for _ in range(t + 1)]  #테이블 만들기
for i in range(t):
    rgb = list(map(int, input().split()))    #r, g, b 개수
    if i ==0 :
        dp[i][0]=rgb[0]
        dp[i][1]=rgb[1]
        dp[i][2]=rgb[2]
    else:
        for j in range(len(rgb)):
            for k in range(len(rgb)):
                if j==k:
                    continue
                else:
                    dp[i][k] = min(dp[i-1][j]+rgb[k] ,dp[i][k])
print(min(dp[t-1]))
