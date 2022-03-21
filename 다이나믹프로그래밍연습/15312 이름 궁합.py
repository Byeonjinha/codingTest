from string import ascii_uppercase
import sys
alpha_list = list(ascii_uppercase)
value_list =  [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1 ]
input = sys.stdin.readline
a = sys.stdin.readline().split()
b = sys.stdin.readline().split()
a=a[0]
b=b[0]
c=""
for i in range(len(a)):
    c+= a[i]
    c+= b[i]
dp = list(map(str,list(c)))
for i in range(len(dp)):
    dp[i] = value_list[alpha_list.index(dp[i])]
for j in range(len(a)+len(b)-2):
    for i in range(len(dp)-1):
        dp[i]=(dp[i]+dp[i+1])%10
dp= str(dp[0])+str(dp[1])
print( ''.join(list(map(str , dp))))