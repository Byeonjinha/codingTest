import sys
a= int(sys.stdin.readline())
b= list(map(int,sys.stdin.readline().split()))
dp = [0 for i in range(a)]
for i in range(len(b)):
    for j in range(i):
        if b[i] > b[j] and dp[i] < dp[j]:
            dp[i]=dp[j]
    dp[i] +=1
print(max(dp))