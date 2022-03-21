import sys
input = sys.stdin.readline
t = int(input())
score =  [0for _ in range(t + 1)]
dp = [0for _ in range(t + 1)]
for i in range(t):
    score[i]= int(input())

for i in range(t):
    if i == 0:
        dp[i]=score[i]
    elif i==1 :
        dp[i]=dp[i-1]+score[i]
    elif i==2 :
        dp[i] = max(score[i-2]+score[i],score[i-1]+score[i])
    else:
        dp[i] = max(dp[i-3]+score[i-1]+score[i],dp[i-2]+score[i])
print(dp[t-1])