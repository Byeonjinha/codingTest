import sys
input = sys.stdin.readline
t = int(input())    #테스트 케이스 만큼 input
for _ in range(t):
    n, m = map(int, input().split())    #다리 서쪽과 동쪽의 개수 input
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]  #테이블 만들기
    # for i in dp:
    #     print(i)
    # print()
    for i in range(1, n + 1):   #1 부터 n까지 
        for j in range(1, m + 1):  #1부터 m까지
            # for k in dp:
            #     print(k)
            # print()
            if i == 1:          # i 가 처음이라면
                dp[i][j] = j       # dp의 i, 칼럼 j 열은 j 가 되고 continue
                continue
            if i == j:
                dp[i][j] = 1      # dp i와 j 가 같다면 dp[i][j] 는 1이됨
            else:
                if j > 1:          # i,j가 같지않고 j가 1보다 크면
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]  #dp[i][j] 는 dp[i][j-1] + dp[i-1][j-1]이 됨
    for k in dp:
        print(k)
    print()
    print(dp[n][m])
