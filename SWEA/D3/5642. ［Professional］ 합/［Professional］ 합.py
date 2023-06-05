T = int(input())
for tc_idx in range(T):
    N = int(input())
    dp = [-1001 for i in range(N)]
    array = list(map(int, input().split()))
    for i in range(len(array)):
        if i == 0: dp[0] = array[0]
        else:
            if dp[i-1] + array[i] <= array[i]: dp[i] = array[i]
            else: dp[i] = dp[i-1] + array[i]
    print("#"+str(tc_idx+1),max(dp))