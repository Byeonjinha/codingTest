fibo_count = 0
def f(n):
    global fibo_count
    DP = [0 for _ in range(n + 1)]
    DP[0], DP[1] = 1, 1
    for i in range(2, n):
        fibo_count += 1
        DP[i] = DP[i - 1] + DP[i - 2]
    return DP[n - 1]

n = int(input())
print(f(n), fibo_count)