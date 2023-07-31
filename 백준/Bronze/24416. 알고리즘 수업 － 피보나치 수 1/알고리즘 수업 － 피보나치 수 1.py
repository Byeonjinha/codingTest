fib_count = 0
fibo_count = 0
def fib(n):
    global fib_count
    if n == 1 or n == 2:
         return 1;  # 코드1
    else:
        fib_count += 1
        return (fib(n - 1) + fib(n - 2));

def fibonacci(n):
    global fibo_count
    f = [0] * (n + 1)
    f[1] = f[2] = 1

    for i in range(3, n + 1):
        fibo_count += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = int(input())
print(fibonacci(n), fibo_count)