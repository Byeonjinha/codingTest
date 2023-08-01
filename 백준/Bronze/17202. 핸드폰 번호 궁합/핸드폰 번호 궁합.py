import sys
input = sys.stdin.readline
a = sys.stdin.readline().split()
b = sys.stdin.readline().split()
a=a[0]
b=b[0]
c=""
dp = [0 for _ in range(len(a)+len(b) + 1)]
for i in range(len(a)):
    c+= a[i]
    c+= b[i]
dp = list(map(int,list(c)))
for j in range(14):
    for i in range(len(dp)-1):
        dp[i]=(dp[i]+dp[i+1])%10
    dp.pop()
print( ''.join(list(map(str , dp ))))


