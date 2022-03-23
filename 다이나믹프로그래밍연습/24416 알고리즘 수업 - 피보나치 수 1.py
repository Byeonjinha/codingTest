count1 = 1
count2 = 0

def fib(n):
    global count1
    if n == 1 or n == 2:
        return 1  # 코드1
    else :
        count1 += 1
        return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
    global count2
    f = [0 for _ in range(n+2)]
    f[1] = 1
    f[2] = 1
    for i in range( 3 , n+1):
        count2 += 1
        f[i] = f[i - 1] + f[i - 2]  # 코드2
    return f[n]

i=9
# fib(i)
# fibonacci(i)
# print(count1,count2)
j= int(input())
dp = [0 for _ in range(47)]
dp2 = [i for i in range(1,48)]
for i in range(1,47):
    if i==1:
        dp[i] = 3
    elif i==2:
        dp[i] = 5
    else:
        dp[i]= dp[i-1]+ dp[i-2]
print(dp[j-3],end=' ')
print(dp2[j-3])