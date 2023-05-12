def solution(triangle):
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0:
                dp[i][j] = triangle[i][j]
            else:
                try:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
                except:
                    continue
    answer = 0
    for i in dp:
        answer = max(answer, max(i))
    
    return answer